import requests, time, re
t1 = time.time()
def spider(url):
    soure = requests.get(url)
    pattern = re.compile(r"(https://.*?[\.]jpg)")
    img_list = re.findall(pattern, soure.text)
    return img_list
imgs = spider('https://movie.douban.com/chart')
for img in imgs:
    print img