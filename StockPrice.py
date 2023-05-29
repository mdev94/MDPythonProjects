import requests
import time

ticker = str(input("Enter the symbol of a stock: "))
api_key = 'c107333c66a049a796401bd050d9b8d3'

def get_stock_price(ticker_symbol, api):
    #ticker_sybol represents the symbol of the stock
    # api represents the api key that goes there(it has all the data)
    url = f"https://api.twelvedata.com/price?symbol={ticker_symbol}&apikey={api}"
    # response is the variable with the data of the company 
    response = requests.get(url).json()
    #the :-3 chops off the last 3 decimal places so it is to nearest hundredth
    price = response['price'][:-3]
    return price


def get_stock_quote(ticker_symbol, api):
    url = f"https://api.twelvedata.com/quote?symbol={ticker_symbol}&apikey={api}"
    response = requests.get(url).json()
    return response

stockdata = get_stock_quote(ticker, api_key)
stock_price = get_stock_price(ticker, api_key)

name = stockdata['name']
print(name, '\nPrice Per Share: $'+stock_price)