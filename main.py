import tweepy
import time
import random
import os
import requests

# Twitter API credentials
bearer_token = "AAAAAAAAAAAAAAAAAAAAAJJH1wEAAAAAbWn0Owivw0YekJBAt0cQptPJVm8%3D9XIYR7ZmfEN71PcmYG6Y18dt8DrG8nFbZrh5MjApIqw17WoNn1"

# Together AI API key from environment variable
together_api_key = os.getenv("TOGETHER_API_KEY")

# Connect to Twitter API v2
client = tweepy.Client(bearer_token=bearer_token)

# Store the ID of the last tweet we responded to
last_seen_id = None

# AI prompt and reply function using Together AI (OpenAI-style)
def generate_ai_roast(tweet_text):
    prompt = f"Someone tweeted: '{tweet_text}'. Write a funny, savage, crypto-style roast reply."
    headers = {
        "Authorization": f"Bearer {together_api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
    response = requests.post("https://api.together.xyz/v1/chat/completions", headers=headers, json=data)
    return response.json()["choices"][0]["message"]["content"].strip()

# Function to check for mentions and reply
def check_mentions():
    global last_seen_id
    query = "@bonkthatfool -is:retweet"
    tweets = client.search_recent_tweets(query=query, since_id=last_seen_id, tweet_fields=['author_id'])

    if tweets.data:
        for tweet in reversed(tweets.data):
            print(f"🔔 Mention from user {tweet.author_id}: {tweet.text}")
            roast = generate_ai_roast(tweet.text)
            try:
                client.create_tweet(in_reply_to_tweet_id=tweet.id, text=roast)
                print("✅ Replied with AI roast!")
                last_seen_id = tweet.id
            except Exception as e:
                print("❌ Error replying:", e)

# Scheduled bonk chaos every 15 minutes
def scheduled_bonk():
    prompt = "Post a funny, savage crypto-themed tweet that sounds like a sentient memecoin bot roasting everyone."
    headers = {
        "Authorization": f"Bearer {together_api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
    response = requests.post("https://api.together.xyz/v1/chat/completions", headers=headers, json=data)
    tweet = response.json()["choices"][0]["message"]["content"].strip()
    try:
        client.create_tweet(text=tweet)
        print("🕒 Scheduled chaos tweeted:", tweet)
    except Exception as e:
        print("❌ Failed to post scheduled tweet:", e)

# Main loop
while True:
    check_mentions()
    scheduled_bonk()
    time.sleep(900)  # 15 minutes

