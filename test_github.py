from bs4 import BeautifulSoup
    url = "https://github.com/{0}?tab=followers".format(username)
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    tem = tmp = soup.find("span", attrs={"class": "f4 link-gray-dark"}).text.strip()