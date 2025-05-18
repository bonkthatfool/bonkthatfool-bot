
import tweepy
import time
import random

# Twitter API credentials (προσοχή: είναι δημόσια στο αρχείο σου!)
api_key = "gLww05TrmL9R2knMQMNlFsDtK"
api_secret = "1924116169386336256-gvm2r659qCOCNS341d67WVKVyk1bjO"
access_token = "1924116169386336256-xrjlb0UhA9kDLFvkxlruTd92UDlHSl"
access_token_secret = "shutJVZwyK0edp1AKR3whVv9yNrfG2mMHYR6OAfkNdxpo"

# Connect to Twitter API
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# 50+ roast-style crypto replies
replies = [
    "You tweeting like it's still 2021 💀",
    "This take is more inflated than Dogecoin 🚀📉",
    "You must be new here... bonk 🤜",
    "Even Vitalik wouldn't approve this nonsense",
    "Your wallet has more dust than your logic",
    "Bro thinks he's Satoshi 🧠",
    "Not even a DAO would vote for that idea",
    "You rugged my brain with this tweet",
    "Bonk that fool, twice for safety",
    "Is your portfolio as empty as this argument?",
    "Go touch grass, not fake charts 🌱📉",
    "This is why the market's down",
    "Your takes age worse than FTX",
    "You mining opinions out of nowhere",
    "This belongs on the blockchain of shame",
    "Bonk that down bad mentality",
    "Even memecoins make more sense than this",
    "This isn't alpha, it's alphabet soup",
    "You're in the wrong layer, chief",
    "This tweet is an NFT of a bad idea",
    "That opinion just got liquidated",
    "You staked your dignity for clout",
    "The gas fees on this take are not worth it",
    "Bonk your keys, not your credibility",
    "Ratio'd by a bot — how embarrassing",
    "Your TA is just astrology with candles",
    "Elon saw this and unsubscribed",
    "Did your seed phrase include this tweet?",
    "Even Bitconnect had more credibility",
    "You're bearish on logic",
    "This tweet belongs in crypto jail 🚓",
    "Stop LARPing as a market analyst",
    "Bonk that ego down to $0.0001",
    "WAGMI? Not with that take",
    "This is a pump and dump of intelligence",
    "Tell me you’re rekt without telling me",
    "Your brain's in cold storage",
    "This tweet needs to be burned — literally 🔥",
    "You missed the block, bro",
    "You’re shorting common sense",
    "This is why we can't have nice chains",
    "Bonk protocol activated",
    "Your logic got 51% attacked",
    "You must be yield farming attention",
    "Your takes are more volatile than Pepe coin",
    "Crypto winter came from tweets like this",
    "Proof of Dumbness achieved",
    "You're deep in the red zone of opinions",
    "Stop staking stupidity",
    "Bonk has entered the chat 🪙",
    "Bro's got a blue check and no clue",
    "This deserves a hard fork from reality",
    "That's not a hot take, that's a burn notice"
]

last_seen_id = None

def check_mentions(last_seen_id):
    mentions = api.mentions_timeline(since_id=last_seen_id, tweet_mode='extended')
    for mention in reversed(mentions):
        print(f"🔔 Mention from @{mention.user.screen_name}: {mention.full_text}")
        response = f"@{mention.user.screen_name} {random.choice(replies)}"
        api.update_status(status=response, in_reply_to_status_id=mention.id)
        print("✅ Replied!")
        last_seen_id = mention.id
    return last_seen_id

while True:
    last_seen_id = check_mentions(last_seen_id)
    time.sleep(30)
