from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
import requests
import pymysql

session = requests.Session()
headers = {"User-Agent": "Mozilla/5.0 (Macintosh Intel Mac OS X 10_9_5) \
                          AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
           "Accept": "text/html,application/xhtml+xml,application/xml;\
                    q=0.9,image/webp,*/*;q=0.8"}


def store(title, url):

    cur.execute(
        "INSERT INTO questions (title, url) VALUES (\"%s\",\"%s\")",
        (title, url))
    cur.connection.commit()


def getTitleUrls(url):
    try:
        req = session.get(url, headers=headers)
    except (HTTPError, URLError) as e:
        return None
    try:
        bsObj = BeautifulSoup(req.text, "html.parser")
        questionLink = bsObj.find_all("div", {"class": "feed-main"})
        for q in questionLink:
            store(q.h2.get_text(),
                  'https://www.zhihu.com' + q.find('a').attrs["href"])
    except AttributeError as e:
        print(e)


if __name__ == '__main__':

    conn = pymysql.connect(host='127.0.0.1', port=3306,
                           user='root', passwd='123456', database='mysql',
                           use_unicode=True, charset="utf8")
    cur = conn.cursor()
    cur.execute("USE scraping")

    start_url = "https://www.zhihu.com/topic/19552832/top-answers"
    getTitleUrls(start_url)

    cur.execute("SELECT * FROM questions")

    cur.close()
    conn.close()
