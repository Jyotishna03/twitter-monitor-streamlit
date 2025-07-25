import requests

bot_token = "8402457588:AAHZ6U7NJmutcpFWVHRL40fBiHKz0__9SVw"
chat_id = "5830229512"  # your user ID
message = "<b>Test Alert</b><br>This is a test message from your bot."

url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

data = {
    "chat_id": chat_id,
    "text": message,
    "parse_mode": "HTML"
}

response = requests.post(url, data=data)
print(response.text)
