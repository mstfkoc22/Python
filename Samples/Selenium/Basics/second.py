from selenium import webdriver

driver = webdriver.Chrome('C:\Coding\Python\drivers\chromedriver.exe')

driver.get('https://www.gittigidiyor.com/ayakkabi?kullanici-tipi=Erkek')

for i in range(1,5):
    name = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[2]/div[3]/div/ul/li['+ str(i) +']/a/div/div/div[1]/div[1]/h3/span').text
    print(name)