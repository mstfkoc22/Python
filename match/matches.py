from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

driver = webdriver.Chrome('C:\Coding\Python\drivers\chromedriver.exe')

driver.get('https://www.mackolik.com/puan-durumu/türkiye-süper-lig/fikstur/482ofyysbdbeoxauk19yg7tdt')

df = pd.DataFrame({'Home_Name':[''], 'Away_Name':[''], 'Home_Team_Rate':[''], 'Draw_Rate':[''], 'Away_Team_Rate':[''], 'Home_Shoot':[''], 'Home_Shoot_Succeed':[''], 'Away_Shoot':[''], 'Away_Shoot_Succeed':[''],
                    '0:0':[''], '0:1':[''], '0:2':[''], '0:3':[''], '0:4':[''], '0:5':[''], '1:0':[''], '1:1':[''], '1:2':[''], '1:3':[''], '1:4':[''], '1:5':[''],
                    '2:0':[''], '2:1':[''], '2:2':[''], '2:3':[''], '2:4':[''], '0:6':[''], '3:0':[''], '3:1':[''], '3:2':[''], '3:3':[''], '4:0':[''], '4:1':[''],
                    '4:2':[''], '5:0':[''], '5:1':[''], '6:0':['']})

soup = BeautifulSoup(driver.page_source, 'lxml')
k = 1
while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    match_codes = soup.find_all('li', class_='p0c-competition-match-list__row')
    for item in match_codes:
        try:
            a = item.find('a')
            
            iddaa = a.get('href').replace(item.attrs['data-match-id'],'iddaa/'+item.attrs['data-match-id'])
            istatistik = a.get('href').replace(item.attrs['data-match-id'],'istatistik/'+item.attrs['data-match-id'])


            driver.get(istatistik)
            try:
                driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div/div/div').click()
            except:
                pass
            driver.find_element_by_xpath('/html/body/div[4]/div[2]/main/div/div[2]/div/div/div[1]/div/div/div/div/div/div/ul/li[3]/a').click()
            Home_Shoot = driver.find_element_by_xpath('/html/body/div[4]/div[2]/main/div/div[2]/div/div/div[1]/div/div/div/div/div/ul/li[3]/div/table/tbody/tr[4]/td[1]').text.strip()
            Home_Shoot_Succeed = driver.find_element_by_xpath('/html/body/div[4]/div[2]/main/div/div[2]/div/div/div[1]/div/div/div/div/div/ul/li[3]/div/table/tbody/tr[6]/td[1]').text.strip()
            Away_Shoot = driver.find_element_by_xpath('/html/body/div[4]/div[2]/main/div/div[2]/div/div/div[1]/div/div/div/div/div/ul/li[3]/div/table/tbody/tr[4]/td[3]').text.strip()
            Away_Shoot_Succeed = driver.find_element_by_xpath('/html/body/div[4]/div[2]/main/div/div[2]/div/div/div[1]/div/div/div/div/div/ul/li[3]/div/table/tbody/tr[6]/td[3]').text.strip()

            driver.get(iddaa)
            try:
                driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div/div/div').click()
            except:
                pass
            Home_Team_Rate = driver.find_element_by_xpath('/html/body/div[4]/div[2]/main/div/div[2]/div/div[2]/div/div[1]/div/ul/li[1]/div/div/ul/li[1]/a/span[2]').text.strip()
            Draw_Rate = driver.find_element_by_xpath('/html/body/div[4]/div[2]/main/div/div[2]/div/div[2]/div/div[1]/div/ul/li[1]/div/div/ul/li[2]/a/span[2]').text.strip()
            Away_Team_Rate = driver.find_element_by_xpath('/html/body/div[4]/div[2]/main/div/div[2]/div/div[2]/div/div[1]/div/ul/li[1]/div/div/ul/li[3]/a/span[2]').text.strip()
            Home_Name = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/div/div[1]/a[1]').text.strip()
            Away_Name = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/div/div[1]/a[2]').text.strip()
            driver.execute_script('window.scrollTo(0,2400)')
                
            score_rates = []
            for i in range(1,29):
                score_rates.append(driver.find_element_by_xpath('/html/body/div[4]/div[2]/main/div/div[2]/div/div[2]/div/div[1]/div/ul/li[21]/div/div/ul/li['+str(i)+']/a/span[2]').text.strip())

            df = df.append({'Home_Name':Home_Name, 'Away_Name':Away_Name, 'Home_Team_Rate':Home_Team_Rate, 'Draw_Rate':Draw_Rate, 'Away_Team_Rate':Away_Team_Rate, 'Home_Shoot':Home_Shoot, 'Home_Shoot_Succeed':Home_Shoot_Succeed, 'Away_Shoot':Away_Shoot, 'Away_Shoot_Succeed':Away_Shoot_Succeed,
                                '0:0':score_rates[0], '0:1':score_rates[1], '0:2':score_rates[2], '0:3':score_rates[3], '0:4':score_rates[4], '0:5':score_rates[5], '1:0':score_rates[6], '1:1':score_rates[7], '1:2':score_rates[8], '1:3':score_rates[9], '1:4':score_rates[10], '1:5':score_rates[11],
                                '2:0':score_rates[12], '2:1':score_rates[13], '2:2':score_rates[14], '2:3':score_rates[15], '2:4':score_rates[16], '0:6':score_rates[17], '3:0':score_rates[18], '3:1':score_rates[19], '3:2':score_rates[20], '3:3':score_rates[21], '4:0':score_rates[22], '4:1':score_rates[23],
                                '4:2':score_rates[24], '5:0':score_rates[25], '5:1':score_rates[26], '6:0':score_rates[27]}, ignore_index = True)
        except:
            pass
                
    try:
        driver.get('https://www.mackolik.com/puan-durumu/türkiye-süper-lig/fikstur/482ofyysbdbeoxauk19yg7tdt')
        time.sleep(3)
        btn = driver.find_element_by_xpath('/html/body/div[4]/div[2]/main/div/div[2]/div/div/div[1]')
        if k >= 3:
            raise Exception('This is the exception you expect to handle')
        for i in range(0,k):
            btn.click()
        k = k+1
        time.sleep(15)
        soup = BeautifulSoup(driver.page_source, 'lxml')
    except:
        df.to_csv('C:/Coding/Python/matches-gg.csv', index=False, encoding='utf-8-sig')
        break