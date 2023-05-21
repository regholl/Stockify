from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
# Create your views here.
def api_fetch(request):
    symbol ='AAPL'
    api_key = 'PY428Q2LKDDX8NC9'
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={api_key}'
    response = request.get(url)
    if response.status_code == 200:
        data = response.json()
        stock = data['Time Series (Daily)']
        return stock
    return None

    



