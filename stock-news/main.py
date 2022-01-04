import requests
from twilio.rest import Client
from nsetools import nse, Nse

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
API_KEY = "VOEWUWSACKCQPNWS"
NEWS_API = "e0d3c54647f547a38cdd4595a07d8ee9"
ACCOUNT_SID = "AC624022be539b9a026318d33c187a3beb"
AUTH_TOKEN = "cd921cb2654ad3e6b64207a6ae6508a4"
dict = {}

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": API_KEY
}
response = requests.get(STOCK_ENDPOINT,params=parameters)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
difference_percent = round((difference / float(yesterday_closing_price)) * 100)
if difference_percent > 5:
    news_parameters = {
        "apiKey": NEWS_API,
        "qInTitle": COMPANY_NAME
    }
    news_response = requests.get(NEWS_ENDPOINT,params=news_parameters)
    articles = news_response.json()["articles"][0:3]
    article_data = [f"{STOCK_NAME}: {up_down}{difference_percent}% \nHeadline: {article['title']}. \nBrief:{article['description']}" for article in articles]
    client = Client(ACCOUNT_SID,AUTH_TOKEN)
    for new_article in article_data:
        message = client.messages \
            .create(
            body=new_article,
            from_='+12568874549',
            to='+919985123453'
        )