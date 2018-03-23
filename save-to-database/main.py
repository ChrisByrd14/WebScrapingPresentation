#!/usr/bin/env python3
'''Simple program to illustrate scraping web data and saving it to a databse
'''

import requests
import sys
from book import Book
from bs4 import BeautifulSoup


URL = 'http://books.toscrape.com'

page = requests.get(URL)

if page.status_code != 200:
    print('{} status code received.\nExiting.'.format(page.status_code))
    sys.exit(1)

soup = BeautifulSoup(page.content, 'html.parser')

products = soup.find_all('article', {'class': 'product_pod'})

product_list = list()
for prod in products:
    # get data fields from the product
    h3 = prod.find('h3')
    title_link = h3.find('a')
    book_title = title_link['title']
    book_url = '{}/{}'.format(URL, title_link['href'])
    book_price = prod.find('p', {'class': 'price_color'}).text.strip('£')

    # only create a database record if each field is not None
    if None not in [book_title, book_url, book_price]:
        Book.create(name=book_title, url=book_url, price=float(book_price))
