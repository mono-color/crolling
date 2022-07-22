# pip install selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
url = 'http://tour.interpark.com/'
driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(3) # 브라우저에서 사용되는 엔진 자체에서 파싱되는 시간을 기다려 주는 메소드
driver.get(url)
# 접속후 페이지가 다 로드되도록 딜레이
time.sleep(1)
driver.find_element(By.ID,'SearchGNBText').send_keys('하와이')
driver.find_element(By.CLASS_NAME,'search-btn').click()
time.sleep(2)

lis = driver.find_elements(By.CSS_SELECTOR, 'li.boxItem')
for li in lis:
    print(li.get_attribute('innerHTML'))
    text = li.text
    print(text)
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(driver.page_source,'html.parser')
# print(soup.prettify())

driver.close()