#!/usr/bin/env python3
'''Simple script to retrieve and print all products from URL
'''
import requests
import bs4
import sys


URL = 'http://books.toscrape.com'
page = requests.get(URL)

if page.status_code != 200:
    print('Got status code {}'.format(page.status_code))
    sys.exit(1)

soup = bs4.BeautifulSoup(page.content, 'html.parser')

# loop over each product and print its text
for product in soup.find_all('article', {'class': 'product_pod'}):
    print(product.text)
