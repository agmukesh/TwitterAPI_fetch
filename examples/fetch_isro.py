"""
Simple example: fetch recent tweets from ISRO using the project's twitter API helper.

How to run (PowerShell):
& E:\twep\venv\Scripts\Activate.ps1
python -m examples.fetch_isro


Requirements:
- Set BEARER_TOKEN in .env in the project root.
- Virtual env activated (optional if running system python that has dependencies).
"""

import json
import sys
from pathlib import Path
from datetime import datetime
from src.api.twitter import search_recent_tweets


def main():
    # Query: tweets from the official ISRO account (no retweets) OR tweets containing the #isro hashtag
    query = "(from:isro -is:retweet) OR #isro"

    try:
        results = search_recent_tweets(query, max_results=10)
    except Exception as e:
        print("Error fetching tweets:", e)
        sys.exit(1)

    data = results.get("data", [])
    meta = results.get("meta", {})

    found = meta.get('result_count', len(data))
    print(f"Found {found} tweets")

    out_dir = Path("outputs")
    out_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    out_file = out_dir / f"isro_tweets_{timestamp}.json"

    try:
        with out_file.open("w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print("Error saving results to file:", e)
        sys.exit(1)

    print(f"Saved results to {out_file.resolve()}")


if __name__ == '__main__':
    main()
