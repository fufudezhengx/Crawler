from urllib.request import urlopen, HTTPError
from bs4 import BeautifulSoup

try:
    html = urlopen("http://pythonscraping.com/pages/page1.html")
except HTTPError as e:
    print(e)
else:
    bsObj = BeautifulSoup(html.read())
    print(bsObj.h1)
