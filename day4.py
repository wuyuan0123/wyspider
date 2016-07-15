from bs4 import BeautifulSoup
import time, requests
def spider(url):
    r = requests.get(url)
    soup = BeautifulSoup(r, "html.parser")
    for link in soup.find_all('img'):
        print(link.get('href'))
t1 = time.time()
spider('https://movie.douban.com/chart')
t2 = time.time
print("time = %.6f sec" % (t2-t1))
