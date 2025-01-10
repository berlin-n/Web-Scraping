import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
}

html_text = requests.get('https://finance.yahoo.com/markets/crypto/gainers/', headers).text
soup = BeautifulSoup(html_text, 'lxml')
token = soup.find('tr', class_="row false yf-paf8n5")
name = token.find('div', class_='yf-eg2gbv').text
symbol = token.find('span', class_='symbol yf-1m808gl').text
marketCap = token.find('fin-streamer', {'data-field': 'marketCap'}).text
percentageChange = token.find('fin-streamer', {'data-field': 'regularMarketChangePercent'}).text
print(f'{name}({symbol}) current Market Cap is {marketCap} and rose by {percentageChange}')