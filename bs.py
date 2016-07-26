from bs4 import BeautifulSoup
import time, requests, re
def spider(url):
    r = requests.get(url)
    #print r.text.encode('utf-8')
    soup = BeautifulSoup(r.text)
    for link in soup.find_all(src=re.compile(r'^https://.*?\.jpg$')):
        try:
            print link.get('alt').encode('utf-8'), link.get('src')
        except AttributeError as e:
            pass
if __name__ ==  '__main__':
    t1 = time.time()
    spider('https://movie.douban.com/chart')
    t2 = time.time()
    print("time = %.6f sec" % (t2 - t1))

