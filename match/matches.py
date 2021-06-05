from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import requests
import time

driver = webdriver.Chrome('C:\Coding\Python\drivers\chromedriver.exe')

res = requests.get('https://www.mackolik.com/puan-durumu/türkiye-süper-lig/fikstur/482ofyysbdbeoxauk19yg7tdt')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.p0c-competition-match-list__status.p0c-competition-match-list__status--post-full-time')

headers = ['Home_Team', 'Away_Team', 'Home_Total_Shoots', 'Home_Accurate_Shoots', 
            'Away_Total_Shoots', 'Away_Accurate_Shoots', 'Home_Win', 'Draw', 'Away_Win']

driver.get(links[0].get('href').replace(links[0].get('href').split('/')[5], 'iddaa/' + links[0].get('href').split('/')[5]))
time.sleep(2)
soup = BeautifulSoup(driver.page_source, 'html.parser')
headers_taken = soup.select('.widget-iddaa-markets__link .widget-iddaa-markets__label')[56:83]
for i in range(0,27):
    headers.append(headers_taken[i].getText().strip().replace(':','-'))

df = pd.DataFrame(columns=headers)

for iter in range(1,3):
    for link in links:
        match_link = link.get('href')
        statistic_link = match_link.replace(match_link.split('/')[5], 'istatistik/' + match_link.split('/')[5])
        bet_link = match_link.replace(match_link.split('/')[5], 'iddaa/' + match_link.split('/')[5])

        match_statistics = []

        driver.get(statistic_link)
        time.sleep(2)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        match_statistics.append(soup.select('.p0c-soccer-match-details-header__team-name.p0c-soccer-match-details-header__team-name--home')[0].getText().strip())
        match_statistics.append(soup.select('.p0c-soccer-match-details-header__team-name.p0c-soccer-match-details-header__team-name--away')[0].getText().strip())

        match_statistics.append(soup.select('.Opta-Outer')[26].getText().strip())
        match_statistics.append(soup.select('.Opta-Outer')[28].getText().strip())
        match_statistics.append(soup.select('.Opta-Outer')[27].getText().strip())
        match_statistics.append(soup.select('.Opta-Outer')[29].getText().strip())


        driver.get(bet_link)
        time.sleep(2)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        match_statistics.append(soup.select('.widget-iddaa-markets__link .widget-iddaa-markets__value')[0].getText().strip())
        match_statistics.append(soup.select('.widget-iddaa-markets__link .widget-iddaa-markets__value')[1].getText().strip())
        match_statistics.append(soup.select('.widget-iddaa-markets__link .widget-iddaa-markets__value')[2].getText().strip())

        match_statistics_taken = soup.select('.widget-iddaa-markets__link .widget-iddaa-markets__value')[56:83]
        
        for i in range(0,27):
            match_statistics.append(match_statistics_taken[i].getText().strip())

        data_to_append = {}
        for i in range(len(df.columns)):
            data_to_append[df.columns[i]] = match_statistics[i]
        df = df.append(data_to_append, ignore_index = True)

    driver.get('https://www.mackolik.com/puan-durumu/türkiye-süper-lig/fikstur/482ofyysbdbeoxauk19yg7tdt')
    for it in range(0,iter):
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/main/div/div[2]/div/div/div[1]').click()
    time.sleep(7)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    links = soup.select('.p0c-competition-match-list__status.p0c-competition-match-list__status--post-full-time')

df.to_csv('C:/Coding/Python/matches-gg.csv', index=False, encoding='utf-8-sig')
driver.quit()