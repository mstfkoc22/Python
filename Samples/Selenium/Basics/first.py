from selenium import webdriver

driver = webdriver.Chrome('C:\Coding\Python\drivers\chromedriver.exe')

driver.get('https://www.gittigidiyor.com/ayakkabi?kullanici-tipi=Erkek')

product_price = driver.find_element_by_xpath('//*[@id="item-info-block-579704025"]/div/div[1]/div[2]/div/div[1]/div/div/div[4]/p').text

driver.find_element_by_xpath('//*[@id="product_id_579704025"]/a').click()