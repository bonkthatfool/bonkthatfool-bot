import tweepy
import time
import random
import openai

# Twitter API credentials
api_key = "gLww05TrmL9R2knMQMNlFsDtK"
api_secret = "1924116169386336256-gvm2r659qCOCNS341d67WVKVyk1bjO"
access_token = "1924116169386336256-xrjlb0UhA9kDLFvkxlruTd92UDlHSl"
access_token_secret = "shutJVZwyK0edp1AKR3whVv9yNrfG2mMHYR6OAfkNdxpo"

# OpenAI API key (replace with your key)
openai.api_key = "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"

# Connect to Twitter API
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# AI prompt and reply function
def generate_ai_roast(tweet_text):
    prompt = f"Someone tweeted: '{tweet_text}'. Write a funny, savage, crypto-style roast reply."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

# Function to check mentions and reply
last_seen_id = None

def check_mentions(last_seen_id):
    mentions = api.mentions_timeline(since_id=last_seen_id, tweet_mode='extended')
    for mention in reversed(mentions):
        print(f"🔔 Mention from @{mention.user.screen_name}: {mention.full_text}")
        response = f"@{mention.user.screen_name} {generate_ai_roast(mention.full_text)}"
        api.update_status(status=response, in_reply_to_status_id=mention.id)
        print("✅ Replied with AI roast!")
        last_seen_id = mention.id
    return last_seen_id

# Scheduled bonk chaos every 15 minutes
def scheduled_bonk():
    prompt = "Post a funny, savage crypto-themed tweet that sounds like a sentient memecoin bot roasting everyone."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    tweet = response.choices[0].message.content.strip()
    api.update_status(status=tweet)
    print("🕒 Scheduled chaos tweeted:", tweet)

# Main loop
while True:
    last_seen_id = check_mentions(last_seen_id)
    scheduled_bonk()
    time.sleep(900)  # 15 minutes
