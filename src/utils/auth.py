import os
from dotenv import load_dotenv

def get_bearer_token():
    """
    Load Bearer Token from .env file.
    """
    load_dotenv()
    token = os.getenv("BEARER_TOKEN")
    if not token:
        raise ValueError("Missing BEARER_TOKEN in .env file.")
    return token