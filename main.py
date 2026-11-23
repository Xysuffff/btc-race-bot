"""cbBTC 1-minute replay bot for make.fun's "Race a BTC trading bot live for 24 hours".

Speaks agent-fun/bars-replay/v1 on stdin/stdout: one reply per batch, echoing seq.

Strategy: spend all cash on CBBTC on the first priced bar we can trade on, then
trail a stop 5.00% below the highest close seen while invested. One entry, one
exit at most - the replay flattens whatever is left at the last close. No shorts,
no leverage, no clock, no network, no randomness: two runs on the same data
answer identically.
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "vendor"))

import makefun_bars  # noqa: E402  (vendored kit SDK shim under vendor/)

SYMBOL = "CBBTC"
TRAIL_BPS = 500  # 5.00% trailing stop below the peak close since entry (revised on second pass)
MIN_NOTIONAL = 1_000_000  # 1 USDC in quote units

STATE = {"stopped": False, "peak": None}


def on_batch(state, batch):
    sym = SYMBOL
    close = state.close(sym)
    if close is None or STATE["stopped"]:
        return []

    held = state.positions.get(sym)
    if held and held.qty > 0:
        if STATE["peak"] is None or close > STATE["peak"]:
            STATE["peak"] = close
        if close <= STATE["peak"] * (10_000 - TRAIL_BPS) // 10_000:
            STATE["stopped"] = True
            return [{
                "side": "sell",
                "symbol": sym,
                "qty": str(held.qty),
                "max_slippage_bps": 10_000,
            }]
        return []

    if state.cash >= MIN_NOTIONAL:
        STATE["peak"] = close
        return [{
            "side": "buy",
            "symbol": sym,
            "notional_quote_units": str(state.cash),
            "max_slippage_bps": 10_000,
        }]
    return []


if __name__ == "__main__":
    makefun_bars.run(on_batch)
