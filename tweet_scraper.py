import snscrape.modules.twitter as sntwitter
import pandas as pd
import os

query = "AI OR artificial intelligence OR machine learning since:2024-01-01 until:2025-01-01"
tweets = []

for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
    if i >= 100:
        break
    tweets.append([tweet.date, tweet.user.username, tweet.content])

df = pd.DataFrame(tweets, columns=["Date", "Username", "Tweet"])

# ✅ Force saving to full path
save_path = r"C:\Users\Jyotishna\Downloads\twitter_dataset_scraper\ai_tweets_sample.csv"
df.to_csv(save_path, index=False)

print(f"✅ Tweets saved to: {save_path}")
