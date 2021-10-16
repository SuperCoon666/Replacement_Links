import sys
import requests
from bs4 import BeautifulSoup
import lxml

url = "https://www.youtube.com/watch?v="
link = "-6JmbdjW-M0"

pars = requests.get(url+link)
soup = str(BeautifulSoup(pars.text, 'lxml'))


#получаем ссылку на канал видео
def get_channel(source):
    sought = 'itemtype="http://schema.org/Person"><link href='
    ind = source.index(sought)+len(sought)

    #finish = 0
    c = 1
    while True:
        if source[ind+c] == '"':
            finish = ind+c+1
            break
        c+=1
        if c>2000:
            return "Couldn't find link channel"


    channel = source[ind:finish]
    return channel


# получаем имя видео
def get_name(source):
    sought = 'YouTube</title><meta content='
    ind = source.index(sought)+len(sought)

    # finish = 0
    c = 1
    while True:
        if source[ind+c] == '"':
            finish = ind+c+1
            break
        c+=1
        if c>2000:
            return "Couldn't find name video"

    name = source[ind:finish]
    return name

print(get_channel(soup))
print(get_name(soup))
