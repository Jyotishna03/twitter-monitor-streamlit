# 🐦 Twitter Scraper for AI Tweet Dataset

This script uses `snscrape` to collect tweets based on the keyword `"AI"` or `"Artificial Intelligence"` and saves them in a CSV file.

## ✅ How to Run

1. Install the dependencies:
```
pip install -r requirements.txt
```

2. Run the script:
```
python tweet_scraper.py
```

3. Output will be:
```
ai_tweets_sample.csv
```

## 🔧 Customize
Edit the `query` inside `tweet_scraper.py` to scrape tweets related to your own keyword or brand.

Example:
```python
query = "YourBrandName lang:en"
```
