import sys
import requests
from bs4 import BeautifulSoup


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
    def new(self, source, name):
        source = source.replace('"', '') + "/videos"
        pars = requests.get(source)
        soup = str(BeautifulSoup(pars.text, 'lxml'))

        while True:
            target = '"title":{"runs":[{"text":' + name
            ind = soup.index(target)
            txt = ""
            c =1
            while True:
                x = soup[ind+len(target)+c]
                if  x== "}":
                    break
                txt +=x
                c+=1

            if "Трансляция закончилась" in txt:
                soup = soup[ind+len(target)+1:]
            else:
                soup = soup[ind+len(target)+1:]
                res_ind = soup.index('"videoId":')+len('"videoId":')
                res = soup[res_ind+1:res_ind+11+1]
                # print(res)
                break

        # print(soup)
        # print(name)
        # print(source)
        # print(txt)
        return res

    def tst(self, link):
        url = "https://www.youtube.com/watch?v="
        pars = requests.get(url+link)
        soup = str(BeautifulSoup(pars.text, 'lxml'))

        r1 = self.get_channel(soup)
        r2 = self.get_name(soup)
        res = self.new(r1, r2)

        return res
