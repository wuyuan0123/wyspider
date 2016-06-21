import requests, time
t1 = time.time()
def spider(url):
    r = requests.get(url)
    # print r.text
    s = "<img"
    count = 0
    start_pos = 0
    flag = 0
    img_list = []

    for i in range(len(r.text)):
        target = r.text[i:i + len(s)]
        if target == s:
            # print target
            for j in range(i, len(r.text)):
                if r.text[j] == '"':
                    if flag == 0:
                        start_pos = j + 1
                        flag = 1
                    else:
                        result = r.text[start_pos: j]
                        flag = 0
                        break
            if result.endswith("jpg"):
                img_list.append(result)

    for i in img_list:
        print i
t2 = time.time()
print("time = %.6f sec" % (t2-t1))

print spider('https://movie.douban.com/chart')
t3 = time.time()
print("time = %.6f sec" % (t3-t1))
print("time = %.6f sec" % (t3-t2)) # t3-t2 = t3 -t1 time = 6.135000 sec