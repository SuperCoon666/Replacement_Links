import sys
import requests
from bs4 import BeautifulSoup
import lxml

from New_Video import New_Video
from Streams_State import Streams_State
# link = "KFHaZAIG2sA"

state = Streams_State('C:\\Users\\Vlad\\Desktop\\Data_Streams.txt')
print("Please wait for the result...")
x = state.get_state()
# print(x)
# for i in range(len(x[0])):
#     print(x[0][i])
# print("Numbers of not working links:"+x[1])
# print("")

rr = x[1].split(",")
new_vid = New_Video()
for i in range(len(x[2])):
    try:
        lin = x[2][i].replace("'", '')
        res = new_vid.tst(lin)
        old = rr[i]+": "+"Old link:"+x[2][i]
        new = "New link:"+res
        print(old, new)
    except:
        print(rr[i]+": "+"We could not find a replacement for this video")
        print("Error: "+ str(sys.exc_info()[1]))
