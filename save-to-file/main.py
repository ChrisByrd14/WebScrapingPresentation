#!/usr/bin/env python3
'''Simple program to illustrate scraping web data and saving it to a file
'''

import csv
import requests
import sys
from bs4 import BeautifulSoup


URL = 'http://books.toscrape.com'

page = requests.get(URL)

if page.status_code != 200:
    print('{} status code received.\nExiting.'.format(page.status_code))
    sys.exit(1)

soup = BeautifulSoup(page.content, 'html.parser')
products = soup.find_all('article', {'class': 'product_pod'})

# create a list of book dictionaries
books = list()
for prod in products:
    book = {}
    book['url'] = prod.find('a')['href']
    h3 = prod.find('h3')
    book['name'] = h3.find('a')['title']
    price_string = prod.find('p', {'class': 'price_color'}).text.strip('£')
    book['price'] = float(price_string)
    books.append(book)

# write a CSV file w/ header row
with open('books.csv', 'w') as file:
    writer = csv.DictWriter(file, sorted(books[0].keys()))
    writer.writeheader()
    writer.writerows(books)
