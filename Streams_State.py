import sys
import requests
from bs4 import BeautifulSoup
import lxml
from collections import defaultdict

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
        numbers = []
        statuses = []
        liars = []
        repeated = {}
        for i in range(len(f)):
            if not f[i].strip():
                continue

            result = self.link_check(f[i])
            statuses.append(result)

            ind = f[i].index("'")
            numb_i = f[i]
            name = numb_i[ind:].replace("\n", '').replace("'", '')
            for j in range(i, len(f)):
                if name not in repeated:
                    repeated[name] = "%s" % numb_i[:ind]
                    continue

                xx = f[j]
                inn = xx.index("'")

                if xx[:inn] in repeated[name]:
                    continue

                if name in xx[inn:]:
                    repeated[name] += "%s" % xx[:inn]
                # print(name, xx[:inn], xx[inn:], xx[inn:] in name  )

            if "False" in result:
                liars.append(numb_i[ind:])
                numb_i = numb_i[:ind]
                numbers.append(numb_i.replace(",", ""))

        gg = [statuses, numbers, liars, repeated]
        return gg
        # print(numbers)
