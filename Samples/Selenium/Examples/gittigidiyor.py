from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

driver = webdriver.Chrome('C:\Coding\Python\drivers\chromedriver.exe')

driver.get('https://www.gittigidiyor.com/uye-girisi')

login_email = driver.find_element_by_xpath('//*[@id="L-UserNameField"]')
login_email.send_keys('masiwas@hotmail.com')

login_password = driver.find_element_by_xpath('//*[@id="L-PasswordField"]')
login_password.send_keys('2471615da')

login_button = driver.find_element_by_xpath('//*[@id="gg-login-enter"]')
login_button.click()

try:
    temp_button = driver.find_element_by_xpath('//*[@id="wis-lightbox"]/button')
    temp_button.click()
except:
    pass

time.sleep(2)
driver.execute_script('window.scrollTo(0,2746)')
all_discounts = driver.find_element_by_xpath('/html/body/div[1]/main/div/div/section[5]/section/div/div/div/div/div/div/div[1]/a')
all_discounts.click()

df = pd.DataFrame({'Link':[''], 'Product':[''], 'Discount':[''], 'Fee':[''], 'Old_Fee':['']})

while True:
    soup = BeautifulSoup(driver.page_source, 'lxml')
    
    time.sleep(2)
    products = soup.find_all('li', class_ = 'gg-uw-6 gg-w-8 gg-d-8 gg-t-8 gg-m-24 gg-mw-12 catalog-seem-cell srp-item-list browser')
    
    for product in products:
        link = product.find('a', class_ = 'product-link').get('href')
        try:
            name = product.find('h3', class_ = 'product-title bold-opt').text.strip()
        except:
            name = product.find('h3', class_ = 'product-title').text.strip()
        try:
            discount = product.find('div', class_ = 'left robotomedium discount-detail discount-percentage').text.strip()
            old_fee = product.find('strike', class_ = 'market-price-sel').text.strip()
            fee = product.find('p', class_ = 'fiyat robotobold price-txt').text.strip()
            if int(discount.split(' ')[0][1:]) > 60:
                df = df.append({'Link':link, 'Product':name, 'Discount':discount, 'Fee':fee, 'Old_Fee': old_fee},
                       ignore_index = True)
        except:
            pass
    
    try:
        button = soup.find('li', class_ = 'next-link').find('a').get('href')
        driver.get('https://www.gittigidiyor.com'+button)
    except:
        break


df.to_csv('C:/Coding/Python/discounts-gg.csv', index=False, encoding='utf-8-sig')