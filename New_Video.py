import sys
import requests
from bs4 import BeautifulSoup
import lxml


class New_Video(object):
    #получаем ссылку на канал видео
    def get_channel(self, source):
        try:
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
        except:
            return "Error: "+ str(sys.exc_info()[1])


    # получаем имя видео
    def get_name(self, source):
        try:
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
        except:
            return "Error: "+ str(sys.exc_info()[1])

    def tst(self, link):
        url = "https://www.youtube.com/watch?v="
        pars = requests.get(url+link)
        soup = str(BeautifulSoup(pars.text, 'lxml'))

        r1 = self.get_channel(soup)
        r2 = self.get_name(soup)

        res = link, r2, r1
        return res
