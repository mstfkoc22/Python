import requests
from bs4 import BeautifulSoup

url = 'http://fragman-tv.com'

page = requests.get(url)
page.text

soup = BeautifulSoup(page.text, 'lxml')
soup

#tags
soup.header
soup.div

#navigatestrings
tag = soup.header.p
tag.string

#attributes
tage = soup.header.a
tag.attrs
tag['data-toggle']
tag['attribute_new'] = 'this is a new attribute'
tag.attrs
print(tag)