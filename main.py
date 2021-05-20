import requests
from newsapi import NewsApiClient

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHA_VANTAGE_KEY = "1CNGY3IVRGZD7VIA"
NEWS_API_KEY = 'c65496c0765f4ab4b2b64d1b4c248dfe'
API_URL = "http://www.alphavantage.co/query"
PARAMETERS = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': 'TSLA',
    'apikey': '1CNGY3IVRGZD7VIA'
}
PARAMETERS_NEWS = {
    'apiKey': NEWS_API_KEY,
    'country': 'us',
    'category': 'business',
    'q': COMPANY_NAME
}


def getNews():
    response = requests.get(
        url='https://newsapi.org/v2/top-headlines', params=PARAMETERS_NEWS)
    response.raise_for_status()
    news = response.json()["articles"]
    news_print = [
        f"Title:{article['title']} \nBrief:{article['description']}"for article in news]
    for i in news_print:
        print(i)


response = requests.get(url=API_URL, params=PARAMETERS)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
daily = [value for (key, value) in data.items()]
yesterday_value = int(float(daily[0]['4. close']))
day_before_yesterday_value = int(float(daily[1]['4. close']))

percentage = abs(int(yesterday_value * 100 / day_before_yesterday_value) - 100)

if percentage >= 5:
    getNews()
