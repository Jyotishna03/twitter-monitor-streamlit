import pandas as pd

# Load tweets with sentiment
df = pd.read_csv('ai_tweets_with_sentiment.csv')

# Filter negative tweets
alerts = df[df['Sentiment'] == 'Negative']

# Display alerts
print("🚨 ALERT: Negative tweets detected!")
for index, row in alerts.iterrows():
    print(f"[{row['Date']}] @{row['Username']} - {row['Tweet']}")
