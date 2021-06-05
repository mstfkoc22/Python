from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

driver = webdriver.Chrome('C:\Coding\Python\drivers\chromedriver.exe')

driver.get('http://www.mackolik.com/puan-durumu/türkiye-süper-lig/fikstur/482ofyysbdbeoxauk19yg7tdt')


time.sleep(2)
df = pd.DataFrame({'Home':[''], 'Hold':[''], 'Away':['']})
while True:
    try:
        try:
            for i in range(1,100):
                login_button = driver.find_element_by_xpath('/html/body/div[4]/div[2]/main/div/div[4]/div[2]/div/div/ol/li/ol/li['+ i +']/div[1]/div[2]')
                login_button.click()
                time.sleep(2)
                soup = BeautifulSoup(driver.page_source, 'lxml')

                time.sleep(2)
                match_links = soup.find_all('a', class_='widget-iddaa-markets__button').get('href')
                        
                print('match links'+match_links)
                for match_link in match_links:
                    driver.get(match_link)
                    soup = BeautifulSoup(driver.page_source, 'lxml')
                    options = soup.find('ul', class_='widget-iddaa-markets__markets-list').find_all('li')
                    home_rate = options[1].find_all('li', 'widget-iddaa-markets__option')[0].find_all('span', 'widget-iddaa-markets__value').text.strip()
                    hold_rate = options[1].find_all('li', 'widget-iddaa-markets__option')[1].find_all('span', 'widget-iddaa-markets__value').text.strip()
                    away_rate = options[1].find_all('li', 'widget-iddaa-markets__option')[2].find_all('span', 'widget-iddaa-markets__value').text.strip()
                    df = df.append({'Home':home_rate, 'Hold':hold_rate, 'Away':away_rate}, ignore_index = True)
        except:
            pass
    except:
        break

df.to_csv('C:/Coding/Python/matches-gg.csv', index=False, encoding='utf-8-sig')
