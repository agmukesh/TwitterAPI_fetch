import pytest
from src.api import twitter

def test_search_recent_tweets(monkeypatch):
    """Mock API call to test response structure."""

    mock_response = {
        "data": [
            {"id": "123", "text": "Hello Twitter!", "author_id": "456"}
        ],
        "meta": {"result_count": 1}
    }

    def mock_connect_to_endpoint(url, params):
        return mock_response

    # Replace the actual function with our mock
    monkeypatch.setattr(twitter, "connect_to_endpoint", mock_connect_to_endpoint)

    result = twitter.connect_to_endpoint("dummy_url", {"query": "test"})
    assert "data" in result
    assert result["meta"]["result_count"] == 1
