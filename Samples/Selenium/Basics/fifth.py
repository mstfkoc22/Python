from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:\Coding\Python\drivers\chromedriver.exe')

driver.get('https://www.google.com/')

box = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')

box.send_keys('anıl atahan')

button = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]')
button.click()

images_button = driver.find_element_by_xpath('/html/body/div[7]/div/div[4]/div/div[1]/div[1]/div[1]/div/div[2]/a')
images_button.click()

total_height = driver.execute_script('return document.body.scrollHeight')
print(total_height)

driver.execute_script('window.scrollTo(0,2746)')

while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')