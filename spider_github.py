from bs4 import BeautifulSoup
import requests
username = "chenyoufu"
url = "https://github.com/{0}?tab=followers".format(username)
r = requests.get(url)
soup = BeautifulSoup(r.text)
tmps = soup.find_all("span", attrs={"class": "f4 link-gray-dark"})
print tmps
print tmps[0].text
user = []
for tmp in tmps:
    user.append(tmp.text)
print user
print len(user)



