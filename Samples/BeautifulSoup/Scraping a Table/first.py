import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.worldometers.info/world-population/'

page = requests.get(url)
page

soup = BeautifulSoup(page.text, 'lxml')
soup

table = soup.find('table', class_='table table-striped table-bordered table-hover table-condensed table-list')
table

table.find_all('th')

headers = []
for i in table.find_all('th'):
    title = i.text.strip()
    headers.append(title)

df = pd.DataFrame(columns = headers)

for j in table.find_all('tr')[1:]:
    row_data = j.find_all('td')
    row = [tr.text.strip() for tr in row_data]
    length = len(df)
    df.loc[length] = row

df.to_csv('C:/Coding/asd.csv')