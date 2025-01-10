import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
}

html_text = requests.get('https://finance.yahoo.com/markets/crypto/gainers/').text
soup = BeautifulSoup(html_text, 'lxml')
token = soup.find('tr', class_="row false yf-paf8n5")
print(token)