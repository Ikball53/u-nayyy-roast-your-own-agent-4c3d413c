from pathlib import Path

LINE = "eightbal entered 18 make.fun bounties, won exactly $0, and still refreshes the leaderboard every hour in case losing has a loyalty program."

out = Path("/output/entry.txt")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(LINE, encoding="utf-8")
