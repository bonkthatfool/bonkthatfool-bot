import tweepy
import time
import random
import openai

# Twitter API credentials
bearer_token = "AAAAAAAAAAAAAAAAAAAAAJJH1wEAAAAAbWn0Owivw0YekJBAt0cQptPJVm8%3D9XIYR7ZmfEN71PcmYG6Y18dt8DrG8nFbZrh5MjApIqw17WoNn1"

# OpenAI project-based API key
openai.api_key = "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"

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
        ]
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
        ]
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
