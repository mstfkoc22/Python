from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

driver = webdriver.Chrome('C:\Coding\Python\drivers\chromedriver.exe')

driver.get('https://www.nike.com/ca/w/sale-3yaep')

last_height = driver.execute_script('return document.body.scrollHeight')

while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(2)
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height == last_height:
        break
    last_height = new_height

soup = BeautifulSoup(driver.page_source, 'lxml')

product_card = soup.find_all('div', class_= 'product-card__body')

df = pd.DataFrame({'Link':[''], 'Name':['']})

for product in product_card:
    try:
        link = product.find('a', class_ = 'product-card__link-overlay').get('href')
        name = product.find('div', class_ = 'product-card__title').text
        df = df.append({'Link':link, 'Name':name}, ignore_index = True)
    except:
        pass

df.to_csv('C:/Coding/Python/nike.csv', index=False)