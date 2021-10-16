import sys
import requests
from bs4 import BeautifulSoup
import lxml

class Streams_State(object):
    def __init__(self, sours):
        self.sours = sours


    def query_date(self, u):
        try:
            url = "https://www.youtube.com/watch?v=" + u
            pars = requests.get(url)
            soup = BeautifulSoup(pars.text, 'lxml')

            if "isLiveNow\":true," in str(soup):
                return "True"
            else:
                return "False"
        except:
            e = sys.exc_info()[1]
            return e

    def link_check(self, start):
        try:
            source = start.replace("\n", '')
            ind = source.index("'")
            link = source[ind:].replace("'",'')
            res = source +" : " + self.query_date(link)
            return res
        except:
            return "Error: "+ str(sys.exc_info()[1])

    def get_state(self):
        f = open(self.sours)
        f = f.readlines()
        numbers = ""
        statuses = []
        liars = []
        for i in range(len(f)):
            if not f[i].strip():
                continue
            result = self.link_check(f[i])
            statuses.append(result)

            if "False" in result:
                ind = f[i].index("'")
                numb_i = f[i]
                liars.append(numb_i[ind:])
                numb_i = numb_i[:ind]
                numbers+= " "+numb_i

        gg = [statuses, numbers, liars]
        return gg
        # print(numbers)
