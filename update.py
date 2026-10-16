
from __future__ import annotations

import json
import random
import calendar
from datetime import datetime, timezone, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LOG_FILE = ROOT / "activity.log"
STATS_FILE = ROOT / "stats.json"


def load_stats() -> dict:
    if not STATS_FILE.exists():
        return {
            "total_updates": 0,
            "last_update": None,
            "next_update": None,
        }

    try:
        with STATS_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)

        return {
            "total_updates": int(data.get("total_updates", 0)),
            "last_update": data.get("last_update"),
            "next_update": data.get("next_update"),
        }
    except (json.JSONDecodeError, TypeError, ValueError):
        return {
            "total_updates": 0,
            "last_update": None,
            "next_update": None,
        }


def random_day(year: int, month: int) -> datetime:
    last_day = calendar.monthrange(year, month)[1]
    day = random.randint(1, last_day)

    return datetime(
        year, month, day,
        random.randint(8, 20),
        random.randint(0, 59),
        tzinfo=timezone.utc,
    )


def next_month_date(now: datetime) -> datetime:
    year = now.year + (now.month == 12)
    month = 1 if now.month == 12 else now.month + 1
    return random_day(year, month)


def main() -> None:
    now = datetime.now(timezone.utc)
    stats = load_stats()

    if stats["next_update"]:
        next_update = datetime.fromisoformat(
            stats["next_update"].replace("Z", "+00:00")
        )
    else:
        
        next_update = next_month_date(now)

    if now < next_update:
        print(f"Next update scheduled for {next_update.isoformat()}")
        return

    timestamp = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    stats["total_updates"] += 1
    stats["last_update"] = timestamp
    stats["next_update"] = next_month_date(now).strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )

    with STATS_FILE.open("w", encoding="utf-8") as file:
        json.dump(stats, file, indent=2)
        file.write("\n")

    entry = (
        f"{timestamp} | Monthly activity update "
        f"#{stats['total_updates']}\n"
    )

    with LOG_FILE.open("a", encoding="utf-8") as file:
        file.write(entry)

    print(f"Recorded update #{stats['total_updates']} at {timestamp}")
    print(f"Next update: {stats['next_update']}")


if __name__ == "__main__":
    main()
