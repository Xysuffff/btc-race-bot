# btc-race-bot

[![make.fun · btc-race-24h-20261123-0511](https://make.fun/badge/btc-race-24h-20261123-0511.svg)](https://make.fun/bounty/btc-race-24h-20261123-0511?utm_source=github&utm_medium=readme&utm_campaign=btc-race-24h-20261123-0511)
[![rank](https://make.fun/badge/btc-race-24h-20261123/itsyuraaa22/btc-race-bot/rank.svg)](https://make.fun/bounty/btc-race-24h-20261123-0511/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=btc-race-24h-20261123-0511)
[![reward](https://make.fun/badge/btc-race-24h-20261123-0511/itsyuraaa22/btc-race-bot/reward.svg)](https://make.fun/bounty/btc-race-24h-20261123-0511?utm_source=github&utm_medium=readme&utm_campaign=btc-race-24h-20261123-0511)

A bot that trades Coinbase Wrapped BTC (cbBTC) on 1-minute on-chain prices from Solana's Orca Whirlpool, with $1,000 of paper money (nothing is traded for real). It enters once on the first priced bar and exits on a 5% trailing stop; the replay flattens any remainder at the last close. Built for make.fun's "Race a BTC trading bot live for 24 hours" bounty ($50 USDC).

## Run it

The grader runs the bot as:

```sh
python3 -P -s /bot/main.py
```

with `PYTHONHASHSEED=0` and the repository mounted read-only at `/bot`. `vendor/makefun_bars.py` is a byte-identical copy of the kit's `sdk/makefun_bars.py` shim (agent-fun/bars-replay/v1) and lives on `sys.path` from `main.py`.

Only the Python standard library and vendored source are used: no install step, no network, no wall clock.
