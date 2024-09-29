import os
import configparser

# Load API key from environment variable or configuration file
api_key = os.environ.get("GOOGLE_API_KEY") or configparser.ConfigParser().get("api_keys", "gemini")

# Use the API key in your code
with ChatSession(api_key=api_key) as session:
    # ...