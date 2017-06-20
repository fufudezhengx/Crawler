from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html)

namelist = bsObj.findAll("span", {"class": "red"})
for name in namelist:
    print(name.getText())
