from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LOG_FILE = ROOT / "activity.log"
STATS_FILE = ROOT / "stats.json"


def load_stats() -> dict:
    if not STATS_FILE.exists():
        return {"total_updates": 0, "last_update": None}

    try:
        with STATS_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)

        return {
            "total_updates": int(data.get("total_updates", 0)),
            "last_update": data.get("last_update"),
        }
    except (json.JSONDecodeError, TypeError, ValueError):
        return {"total_updates": 0, "last_update": None}


def main() -> None:
    now = datetime.now(timezone.utc)
    timestamp = now.strftime("%Y-%m-%dT%H:%M:%SZ")

    stats = load_stats()
    stats["total_updates"] += 1
    stats["last_update"] = timestamp

    with STATS_FILE.open("w", encoding="utf-8") as file:
        json.dump(stats, file, indent=2)
        file.write("\n")

    entry = f"{timestamp} | Daily activity update #{stats['total_updates']}\n"

    with LOG_FILE.open("a", encoding="utf-8") as file:
        file.write(entry)

    print(f"Recorded update #{stats['total_updates']} at {timestamp}")


if __name__ == "__main__":
    main()
