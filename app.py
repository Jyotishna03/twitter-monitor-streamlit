import streamlit as st
import pandas as pd
import requests
from textblob import TextBlob

# --- CONFIGURATION ---
BOT_TOKEN = "8402457588:AAHZ6U7NJmutcpFWVHRL40fBiHKz0__9SVw"
CHAT_ID = "5830229512"
CSV_FILE = "ai_tweets_sample.csv"

# --- THEME FUNCTION ---
def apply_theme(theme="light"):
    if theme == "dark":
        st.markdown(
            """
            <style>
            body { background-color: #0e1117; color: white; }
            .stApp { background-color: #0e1117; color: white; }
            div[data-testid="stMarkdownContainer"] { color: white; }
            </style>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            """
            <style>
            .stApp { background-color: white; color: black; }
            div[data-testid="stMarkdownContainer"] { color: black; }
            </style>
            """,
            unsafe_allow_html=True
        )

# --- MAIN APP ---
st.set_page_config(page_title="Tweet Sentiment Monitor", layout="centered")
st.title("-Monitor Twitter in Real-Time-")

# Theme Selector
theme = st.selectbox("🎨 Select Theme", ["light", "dark"])
apply_theme(theme)

# Upload CSV or use default
uploaded_file = st.file_uploader("📂 Upload tweet CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    try:
        df = pd.read_csv(CSV_FILE)
    except:
        st.error("No CSV file found. Please upload one.")
        st.stop()

# Show columns and preview
st.subheader("📊 Data Preview")
st.write(df.head())

# --- Sentiment Analysis ---
def get_sentiment(text):
    blob = TextBlob(str(text))
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "positive"
    elif polarity < 0:
        return "negative"
    else:
        return "neutral"

if st.button("🔍 Run Sentiment Analysis"):
    with st.spinner("Analyzing tweets..."):
        df["sentiment"] = df["Tweet"].astype(str).apply(get_sentiment)
        df.to_csv("alert_tweets.csv", index=False)
        st.success("✅ Analysis complete. Saved to alert_tweets.csv")

        # Show result
        st.write(df.head())

        # --- Alerting ---
        st.subheader("📤 Sending Alerts for Negative Tweets")
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

        neg_tweets = df[df["sentiment"] == "negative"]["Tweet"].head(5)
        for tweet in neg_tweets:
            data = {
                "chat_id": CHAT_ID,
                "text": f"<b>🚨 Negative Tweet Detected</b>\n{tweet}",
                "parse_mode": "HTML"
            }
            try:
                response = requests.post(url, data=data, timeout=10)
                if response.status_code == 200:
                    st.success("✅ Alert sent")
                else:
                    st.error(f"❌ Failed to send: {response.text}")
            except Exception as e:
                st.error(f"❌ Network error: {e}")
