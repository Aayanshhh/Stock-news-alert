# Stock-news-alert

This project fetches the closing price of Tesla Inc. (TSLA) stock, calculates the percentage difference between the latest two closing prices, and if the difference is greater than 1%, sends the latest news articles about Tesla Inc. via SMS using the Twilio API.

## Features

- Fetch the latest closing prices for TSLA stock using the Alpha Vantage API.
- Calculate the percentage difference between the last two closing prices.
- Fetch the latest news articles about Tesla Inc. if the percentage difference is greater than 1%.
- Send the news articles via SMS using the Twilio API.

## Setup

### Prerequisites

- Python 3.x
- `requests` library
- `twilio` library

## Configuration
Replace the placeholder values in the script with your actual credentials and phone numbers:

- STOCK_API_KEY = "your_alpha_vantage_api_key"
- NEWS_API_KEY = "your_news_api_key"
- TWILIO_SID = "your_twilio_account_sid"
- TWILIO_AUTH_TOKEN = "your_twilio_auth_token"<br>

Also, replace the from and to phone numbers in the Twilio message creation section:

## How It Works
- The script fetches the daily time series data for TSLA stock from the Alpha Vantage API.
- It extracts the closing prices for the last two days.
- It calculates the absolute and percentage difference between the two closing prices.
- If the percentage difference is greater than 1%, the script fetches the latest news articles about Tesla Inc. from the News API.
- The top 3 news articles are formatted and sent via SMS using the Twilio API.
