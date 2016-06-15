import requests, time, re
t1 = time.time()
def spider(url):
    soure = requests.get(url)
    pattern = re.compile(r"^https:[0-9a-zA-Z\/\.\s]+jpg$")
    img_list = re.search(pattern, soure)
    if img_list:
        print img_list.group()
    else:
        pass
    return img_list
    print img_list
print spider('https://movie.douban.com/chart')

