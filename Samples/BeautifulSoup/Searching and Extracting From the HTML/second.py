import requests
from bs4 import BeautifulSoup

url = 'http://fragman-tv.com'

page = requests.get(url)
page.text

soup = BeautifulSoup(page.text, 'lxml')
soup

#find
soup.find('header')
soup.header.atrs

soup.find('div', {'class':'container test-site'})
soup.find('h4', {'class':'pull-right price'})
soup.find('h4', class_='pull-right price')

#findall 1
soup.find_all('h4', {'class':'pull-right price'})
soup.find_all('h4', {'class':'pull-right price'})[1]
soup.find_all('h4', {'class':'pull-right price'})[6:]
soup.find_all('a', class_='title')
soup.find_all('p', class_='pull-right')

#findall 2
soup.find_all(['h4','p','a'])
soup.find_all(id = True)
soup.find_all(string = 'iphone')

import re
soup.find_all(string = re.compile('iph'))
soup.find_all(string = ['Iphone', 'Nokia 123'])
soup.find_all(class_ = re.compile('pull'))
soup.find_all('p', class_ = re.compile('pull'))
soup.find_all('p', class_ = re.compile('pull'), limit = 2)

#findall 3
product_name = soup.find_all('a', class_ = 'title')
product_name

price = soup.find_all('h4', class_ = 'pull-right price')
price

reviews = soup.find_all('p', class_ = re.compile('pull'))
reviews

descriptions = soup.find_all('p', class_ = 'description')
descriptions

product_name_list = []
for i in product_name:
    name = i.text
    product_name_list.append(name)

price_list = []
for i in price:
    price2 = i.text
    price_list.append(price2)

reviews_list = []
for i in reviews:
    reviews2 = i.text
    reviews_list.append(reviews2)

descriptions_list = []
for i in descriptions:
    descriptions2 = i.text
    descriptions_list.append(descriptions2)

import pandas as pd

table = pd.DataFrame({'Product Name': product_name_list, 'Description': descriptions_list,
                     'Prices': price_list, 'Reviews': reviews_list})


#extracted data from nested HTML Tags

boxes = soup.find_all('div', class_ = 'col-sm-4 col-lg-4 col-md-4')[6]
boxes

boxes.find('a').text

boxes.find('p', class_='description').text

box2 = soup.find_all('ul', class_='nav', id='side-menu')[0]

box2.find_all('li')[i].text