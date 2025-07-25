import pandas as pd
import requests
from textblob import TextBlob

# Load tweet data
df = pd.read_csv("ai_tweets_sample.csv")
print("🧾 Columns in your CSV:")
print(df.columns)

print("📄 Tweets loaded from ai_tweets_sample.csv")

# Step 1: Sentiment Analysis
def get_sentiment(text):
    blob = TextBlob(str(text))
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "positive"
    elif polarity < 0:
        return "negative"
    else:
        return "neutral"

df["sentiment"] = df["Tweet"].apply(get_sentiment)

# Step 2: Save to new CSV
df.to_csv("alert_tweets.csv", index=False)
print("✅ Saved results to alert_tweets.csv")

# Step 3: Telegram Alerting (only for negative tweets)
bot_token = "8402457588:AAHZ6U7NJmutcpFWVHRL40fBiHKz0__9SVw"
chat_id = "5830229512"
url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

for tweet in df[df["sentiment"] == "negative"]["Tweet"].head(5):  # limit to 5 alerts
    message = f"<b>🚨 Negative Tweet Detected:</b>\n{tweet}"
    data = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "HTML"
    }
    try:
        response = requests.post(url, data=data, timeout=10)
        if response.status_code == 200:
            print("✅ Alert sent")
        else:
            print(f"❌ Failed to send alert: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Network error: {e}")
