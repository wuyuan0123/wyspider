import requests, time, re
def spider(url):
    soure = requests.get(url)
    pattern = re.compile(r"(https://.*?[\.]jpg)")
    img_list = re.findall(pattern, soure.text)
    return img_list
t1 = time.time()
imgs = spider('https://movie.douban.com/chart')
t2 = time.time()
for img in imgs:
    print img
t3 = time.time()
print("time = %.6f sec" % (t2-t1))
print("time = %.6f sec" % (t3-t1))  #result : t3-t1 = t2 -t1 time = 0.671000 sec


