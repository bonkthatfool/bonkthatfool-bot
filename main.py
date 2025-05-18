import tweepy
import time
import random
import openai

# Twitter API credentials
bearer_token = "AAAAAAAAAAAAAAAAAAAAAJJH1wEAAAAAbWn0Owivw0YekJBAt0cQptPJVm8%3D9XIYR7ZmfEN71PcmYG6Y18dt8DrG8nFbZrh5MjApIqw17WoNn1"

# OpenAI project-based API key
openai.api_key = "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"

# Project ID
project_id = "proj_OuWbXmHyrSTw6SJY2g1guCAZ"

# Connect to Twitter API v2
client = tweepy.Client(bearer_token=bearer_token)

# Store the ID of the last tweet we responded to
last_seen_id = None

# AI prompt and reply function using project-based OpenAI key
def generate_ai_roast(tweet_text):
    prompt = f"Someone tweeted: '{tweet_text}'. Write a funny, savage, crypto-style roast reply."
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        project=project_id
    )
    return response.choices[0].message.content.strip()

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
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        project=project_id
    )
    tweet = response.choices[0].message.content.strip()
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
