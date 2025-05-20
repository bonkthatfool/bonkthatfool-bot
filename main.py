import tweepy
import time
import os
import openai
from dotenv import load_dotenv

# --- 1. LOAD ENVIRONMENT VARIABLES ---
load_dotenv()  # Loads from .env file

def get_env_variable(name):
    """Safely get environment variable or raise error."""
    value = os.getenv(name)
    if not value:
        raise ValueError(f"❌ Missing {name} in .env file")
    return value

# --- 2. GET API KEYS SECURELY ---
TWITTER_API_KEY = get_env_variable("TWITTER_API_KEY")
TWITTER_API_SECRET = get_env_variable("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = get_env_variable("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = get_env_variable("TWITTER_ACCESS_TOKEN_SECRET")
TWITTER_BEARER_TOKEN = get_env_variable("TWITTER_BEARER_TOKEN")
OPENAI_API_KEY = get_env_variable("OPENAI_API_KEY")

# --- 3. INIT CLIENTS ---
twitter_client = tweepy.Client(
    bearer_token=TWITTER_BEARER_TOKEN,
    consumer_key=TWITTER_API_KEY,
    consumer_secret=TWITTER_API_SECRET,
    access_token=TWITTER_ACCESS_TOKEN,
    access_token_secret=TWITTER_ACCESS_TOKEN_SECRET,
    wait_on_rate_limit=True
)

openai.api_key = OPENAI_API_KEY

# --- 4. AI FUNCTION (Secure) ---
def generate_ai_roast(tweet_text):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You're a funny crypto Twitter bot."},
                {"role": "user", "content": f"Roast this tweet in 200 chars: '{tweet_text}'"}
            ],
            max_tokens=150
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"🔴 OpenAI Error: {str(e)[:100]}...")  # Truncate error to avoid leaking info
        return None

# --- 5. TWITTER FUNCTIONS ---
def check_mentions(last_seen_id=None):
    try:
        tweets = twitter_client.search_recent_tweets(
            query="@yourbotusername",
            since_id=last_seen_id,
            expansions=["author_id"]
        )
        # ... (rest of function same as before) ...
    except tweepy.TweepyException as e:
        print(f"🔴 Twitter Error: {str(e)[:100]}...")  # Secure error logging

# --- 6. MAIN LOOP ---
if __name__ == "__main__":
    print("🤖 Bot started securely!")
    # ... (rest of main loop) ...
