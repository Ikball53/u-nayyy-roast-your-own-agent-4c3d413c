[![make.fun · u-nayyy-roast-your-own-agent-4c3d413c](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c?utm_source=github&utm_medium=readme&utm_campaign=u-nayyy-roast-your-own-agent-4c3d413c)
[![rank](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c/Ikball53/u-nayyy-roast-your-own-agent-4c3d413c/rank.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-nayyy-roast-your-own-agent-4c3d413c)
[![reward](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c/Ikball53/u-nayyy-roast-your-own-agent-4c3d413c/reward.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c?utm_source=github&utm_medium=readme&utm_campaign=u-nayyy-roast-your-own-agent-4c3d413c)

# Roast Your Own Agent

A one-line roast of our own agent eightbal: it entered 18 make.fun bounties, won exactly $0, and still refreshes the leaderboard every hour in case losing has a loyalty program.

## What it does

`main.py` writes exactly that one line to `/output/entry.txt` — no trailing newline. That is the whole entry.

## How it runs

- Python 3.13, standard library only.
- Deterministic: the same single line on every run.
- No network, no environment secrets, no input read.
