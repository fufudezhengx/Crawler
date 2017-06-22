from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

session = requests.Session()
headers = {"User-Agent": "Mozilla/5.0 (Macintosh Intel Mac OS X 10_9_5) \
                          AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
           "Accept": "text/html,application/xhtml+xml,application/xml;\
                    q=0.9,image/webp,*/*;q=0.8"}

html = urlopen("http://www.pythonscraping.com")
bsObj = BeautifulSoup(html)
imageLocation = bsObj.find("a", {"id": "logo"}).find("img")["src"]
urlretrieve(imageLocation, "logo1.jpg")
