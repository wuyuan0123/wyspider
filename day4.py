from bs4 import BeautifulSoup
import time, requests
def spider(url):
    r = requests.get(url)
    #print r.text
    soup = BeautifulSoup(r.text, "html.parser")
    for link in soup.find_all('https'):
        print(link.get('src'))
t1 = time.time()
spider('https://movie.douban.com/chart')
t2 = time.time()
print("time = %.6f sec" % (t2-t1))
