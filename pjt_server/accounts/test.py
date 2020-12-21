from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from urllib.parse import quote_plus
import random

baseUrl = 'http://random.cat/view/'
plusUrl = str(random.randint(1, 1500))
url = baseUrl + plusUrl
html = urlopen(url)
soup = bs(html, "html.parser")
img = soup.find_all(id='cat')
imgUrl = img[0]['src']