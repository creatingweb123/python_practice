from datetime import date, timedelta
import requests
from twilio.rest import Client
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

account_sid = os.environ.get("account_sid")
auth_token = os.environ.get("auth_token")

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
NEWS_API_KEY  = os.environ.get("NEWS_API_KEY")

today = date.today()
yesterday = today - timedelta(days=1)
day_before_yesterday = today - timedelta(days=2)

stock_params = {
    "function"      : "TIME_SERIES_DAILY",
    "symbol"        : STOCK,
    "apikey"        : STOCK_API_KEY
}
news_params = {
    "apiKey"    : NEWS_API_KEY,
    "q"         : STOCK,
    "searchIn"  : "title",
    "from"      : f"{day_before_yesterday}",
    "to"        : f"{yesterday}",
    "language"  : "en",
    "sortBy"    : "relevancy"
}

def get_news(increase_decrease_value):
    brief_letter = ""
    news_response = requests.get(url=NEWS_ENDPOINT,params = news_params)
    news_response.raise_for_status()
    news_articles = news_response.json()["articles"]
    for news_article in news_articles:
        headline     = news_article["title"]
        description  = news_article["description"] 
        if increase_decrease_value > 0 :
            brief_letter += f"{STOCK}: 🔺{increase_decrease_value}%\n"
        else:
            brief_letter += f"{STOCK}: 🔻{increase_decrease_value}%\n"
        brief_letter += f"HeadLine : {headline}\nBrief    : {description}\n\n"
    return brief_letter

stock_response = requests.get(url=STOCK_ENDPOINT,params=stock_params)
stock_response.raise_for_status()
data_list = []
recent_data = stock_response.json()["Time Series (Daily)"][yesterday]["4. close"]
before_recent_data = stock_response.json()["Time Series (Daily)"][day_before_yesterday]["4. close"]

increase_decrease_value = float(recent_data) - float(before_recent_data)
diff_percent = round(abs(increase_decrease_value)/float(before_recent_data))*100
if diff_percent>1:
    information = get_news(increase_decrease_value)
    client = Client(account_sid,auth_token)
    message = client.messages.create(
        body    = information,
        from_   = os.environ.get("from_")
        to      = os.environ.get("to")
    )
    print(message.sid)
