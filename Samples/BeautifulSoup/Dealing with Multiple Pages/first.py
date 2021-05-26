import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.airbnb.com.tr/s/homes?refinement_paths%5B%5D=%2Fhomes%2Fsection%2FNEARBY_LISTINGS%3A483&room_types%5B%5D=Entire%20home%2Fapt&property_type_id%5B%5D=57&property_type_id%5B%5D=4&property_type_id%5B%5D=32&property_type_id%5B%5D=58&property_type_id%5B%5D=18&property_type_id%5B%5D=22&property_type_id%5B%5D=17&property_type_id%5B%5D=23&property_type_id%5B%5D=63&property_type_id%5B%5D=24&property_type_id%5B%5D=12&property_type_id%5B%5D=19&property_type_id%5B%5D=44&property_type_id%5B%5D=66&property_type_id%5B%5D=34&property_type_id%5B%5D=16&property_type_id%5B%5D=6&property_type_id%5B%5D=69&property_type_id%5B%5D=15&title_type=CURATED_PROPERTY_TYPE'

page = requests.get(url)
page

soup = BeautifulSoup(page.text, 'lxml')
soup

df = pd.DataFrame({'Links': [''], 'Title': [''], 'Details': [''],
                    'Price': [''], 'Rating': ['']})

while True:
    postings = soup.find_all('div', class_='_8ssblpx')
    for post in postings:
        try:
            link = post.find('a', class_='_mm360j').get('href')
            link_full = 'https://www.airbnb.com.tr' + link
            title = post.find('div', class_='_b14dlit').text
            price = post.find('span', class_='_krjbj').text
            rating = post.find('span', class_='_10fy1f8').text
            details = post.find_all('div', class_='_kqh46o')[0].text
            df = df.append({'Links':link_full, 'Title':title,
                                'Details':details, 'Price':price,
                                'Rating':rating}, ignore_index=True)
        except:
            pass

    try:
        next_page = soup.find('a', {'aria-label':'Sonraki'}).get('href')
        next_page_full = 'https://www.airbnb.com.tr'+next_page
        next_page_full

        url = next_page_full
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'lxml')
    except:
        break


df.to_csv('C:/Coding/Python/asd.csv', encoding='utf-8-sig')