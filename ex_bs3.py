from bs4 import BeautifulSoup
import requests

url = 'https://www.msn.com/ko-kr/news'
res = requests.get(url)
