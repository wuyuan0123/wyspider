from bs4 import BeautifulSoup
import requests
users_list= []

def get_user(username):
    global users_list
    users = []
    url = "https://github.com/{0}?tab=followers".format(username)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    tmps = soup.find_all("span", attrs={"class": "link-gray pl-1"})
    for tmp in tmps:
        users.append(tmp.text)
    for tmp in tmps:
        if tmp.text not in users_list:
            users_list.append(tmp.text)
    return users,len(users)



print get_user("chenyoufu")

for user in users_list:
    print user
    get_user(user)
    print users_list
    print len(users_list)












