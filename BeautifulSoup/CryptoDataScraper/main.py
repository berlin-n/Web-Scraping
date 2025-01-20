import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
}

base_url = "https://finance.yahoo.com/markets/crypto/gainers/?start="
count = "&count=25"

def scrape(base_url, max_pages):
    all_data = []
    for page in range(0, max_pages, 25):
        url = f"{base_url}{page}{count}"
        print(f"Scraping page {page}: {url}")

        # html_text = requests.get(url, headers).text
        # soup = BeautifulSoup(html_text, 'lxml')
        # tokens  = soup.find_all('tr', class_="row false yf-paf8n5")
        # for index, token in enumerate(tokens):
        #     name = token.find('div', class_='yf-eg2gbv').text
        #     symbol = token.find('span', class_='symbol yf-1m808gl').text
        #     marketCap = token.find('fin-streamer', {'data-field': 'marketCap'}).text
        #     percentageChange = token.find('fin-streamer', {'data-field': 'regularMarketChangePercent'}).text
        #     print(f'{name},({symbol}) current Market Cap is {marketCap} and rose by {percentageChange}')
        #     with open('crypto-gainers.csv', 'w', newline=' ') as file:
        #         writer = csv.writer(file)
        #         writer.writerow(['Name','Symbol','Market Cap','Percentage Change'])

scrape(base_url, 914)