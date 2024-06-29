import requests
from twilio.rest import Client
import os
# Define constants
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = os.getenv("STOCK_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

# Get stock data
stock_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK_NAME}&apikey={STOCK_API_KEY}"
stock_response = requests.get(stock_url)
stock_data = stock_response.json()["Time Series (Daily)"]

# Extract closing prices
data_list = [value for (key, value) in stock_data.items()]
yesterday_data = data_list[0]
day_before_yesterday_data = data_list[1]

yesterday_closing_price = float(yesterday_data["4. close"])
print(yesterday_closing_price)
day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])
print(day_before_yesterday_closing_price)
# Calculate price difference
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "↑"
else:
    up_down = "↓"

diff_perc = round((difference / yesterday_closing_price) * 100)

# Check if the difference percentage is greater than 1%
if abs(diff_perc) > 1:
    # Get news articles
    news_url = f"https://newsapi.org/v2/everything?qInTitle={COMPANY_NAME}&apiKey={NEWS_API_KEY}"
    news_response = requests.get(news_url)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]

        # Format articles
    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_perc}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
        # Send SMS with Twilio
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_='+12765657787',
            to="+917007400374"
        )
        print(f"Message sent: {message.sid}")
