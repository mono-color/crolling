import csv

from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(3)
driver.get('https://www.msn.com/ko-kr/news?cvid=2bec1b6f27f641d69099a2c580920383')
try:
    data = []
    cnt = 20
    pagedown = 1
    body = driver.find_element(By.TAG_NAME,'body')
    while pagedown < cnt:
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        pagedown += 1
        #스크롤을 내린 후 bs4로 파싱하여
        # 기사 href와 제목을 txt or csv 저장하시오
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        content = soup.select_one('.riverSections-DS-EntryPoint1-1')
        divs = content.select('.contentCard_headingContainer-DS-card1-1')
        for div in divs:
            a = div.select('a')
            title = a[1].text
            href = a[1].get('href')
            data.append([title,href])

        with open('news.csv', 'w', encoding='utf-8') as f:
            write = csv.writer(f, delimiter='|', quotechar='"')
            for i in data:
                write.writerow(i)
except Exception as e:
    print(str(e))
driver.close()