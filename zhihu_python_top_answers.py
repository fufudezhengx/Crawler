from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
import requests
import re

session = requests.Session()
headers = {"User-Agent": "Mozilla/5.0 (Macintosh Intel Mac OS X 10_9_5) \
                          AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
           "Accept": "text/html,application/xhtml+xml,application/xml;\
                    q=0.9,image/webp,*/*;q=0.8"}


def getUrls(url):
    try:
        html = urlopen(url)
    except (HTTPError, URLError) as e:
        return None
    try:
        bsObj = BeautifulSoup(html)
        a_tags = bsObj.find_all(
            "a", {"href": re.compile(r'/question/[0-9]*$')})
        UrlList = []
        for a in a_tags:
            UrlList.append('https://www.zhihu.com' + a.attrs['href'])
    except AttributeError as e:
        return None
    return UrlList


if __name__ == '__main__':

    start_url = "https://www.zhihu.com/topic/19552832/top-answers"
    urls = getUrls(start_url)
    if urls == None:
        print("Urls could not find")
    else:
        print(urls)
