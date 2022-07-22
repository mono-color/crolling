# https://namu.wiki/w/%EC%9C%A4%EB%8F%99%EC%A3%BC
from bs4 import BeautifulSoup
from urllib import parse
import urllib.request as req

query = '저자:윤동주'
print('url 인코딩:', parse.quote(query))
print('url 인코딩:', parse.unquote('%EC%A0%80%EC%9E%90%3A%EC%9C%A4%EB%8F%99%EC%A3%BC'))
url = 'https://namu.wiki/' + parse.quote(query)
# url = 'https://namu.wiki/' + query #오류남
res = req.urlopen(url)
soup = BeautifulSoup(res, 'html.parser')
print(soup.prettify())
