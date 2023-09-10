import requests
from bs4 import BeautifulSoup
import sqlite3
from datetime import datetime

url = 'https://www.sulpak.kg/f/noutbuki'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

products = soup.find_all('div', class_='b-offer-tiles-item__wrap')

connect = sqlite3.connect('laptops.db')
cursor = connect.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS laptops 
(id INTEGER PRIMARY KEY AUTOINCREMENT, 
title TEXT, 
price TEXT, 
created TEXT)''')

for product in products:
    title = product.find('a', class_='b-offer-tiles-item__name').text.strip()

    price = product.find('div', class_='b-offer-tiles-item__price-new').text.strip()

    created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute('INSERT INTO laptops (title, price, created) VALUES (?, ?, ?)', (title, price, created))

connect.commit()

connect.close()