import pandas as pd
import streamlit as st

# Load data
df = pd.read_csv('ai_tweets_with_sentiment.csv')

st.title("📊 AI Tweet Sentiment Dashboard")
st.write("Visualize sentiments of tweets related to AI and Machine Learning.")

# Sentiment counts
sentiment_counts = df['Sentiment'].value_counts()
st.subheader("Sentiment Distribution")
st.bar_chart(sentiment_counts)

# Show all tweets
if st.checkbox("Show All Tweets"):
    st.dataframe(df)

# Show only Negative
if st.checkbox("Show Only Negative Alerts"):
    st.dataframe(df[df['Sentiment'] == 'Negative'])
