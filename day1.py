__author__ = 'wuyuan'
# -*- coding: utf-8 -*-
import requests
r = requests.get('https://movie.douban.com/tag/2014')
print r.text
img_patten = '<img src="https'
start, end = 0, 0
count = 0


def day1():
    for i in range(0, len(r.text)):
        x = r.text[i:i+len(img_patten)]
        if x == img_patten:
            # print x
            for j in range(i, len(r.text)):
                if r.text[j] == '"':
                    if count == 0:
                        start = j
                        count = 1
                    elif count == 1:
                        xxx = r.text[start:j]
                        print xxx
                        count = 0
                        break

day1()

