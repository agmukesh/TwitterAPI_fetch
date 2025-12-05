import requests
import json
from src.utils.auth import get_bearer_token

SEARCH_URL = "https://api.twitter.com/2/tweets/search/recent"

def bearer_oauth(r):
    """
    Adds Bearer Token authentication headers to a request.
    """
    token = get_bearer_token()
    r.headers["Authorization"] = f"Bearer {token}"
    r.headers["User-Agent"] = "twepClient"
    return r


def connect_to_endpoint(url, params):
    """
    Connect to Twitter API endpoint and return parsed JSON.
    """
    response = requests.get(url, auth=bearer_oauth, params=params)
    print(f"Status code: {response.status_code}")

    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def search_recent_tweets(query, max_results=10):
    """
    Search recent tweets based on query string.
    """
    params = {
      "query": query,
     "max_results": max_results,
     "tweet.fields": "author_id,created_at,text,public_metrics",
     "expansions": "author_id",
     "user.fields": "username,name"
    }
    result = connect_to_endpoint(SEARCH_URL, params)
    return result


if __name__ == "__main__":
    # Example usage
    response = search_recent_tweets("(from:twitterdev -is:retweet) OR #twitterdev")
    print(json.dumps(response, indent=4, sort_keys=True))
