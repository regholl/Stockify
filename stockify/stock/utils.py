import requests
import json
import yfinance as yf

def stock_fetch_api(symbols):
    stock_data = {}
    for symbol in symbols:
        stock = yf.Ticker(symbol)
        data = stock.history(period="1d")
        stock_data[symbol] = data.to_dict(orient='list')
    
    datas ={}
    for key,val in stock_data.items():
        datas[key] =[]
        for stk,price in val.items():
            price = round(price[0],3)
            datas[key].append(price)
   
    return datas

def unit_price_fetch(symbol):
    stock = yf.Ticker(symbol)
    data = stock.history(period="1d")
    data = data.to_dict(orient='records')
    unit_price = round(data[0]['Open'],5)
    return unit_price






    


