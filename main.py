import sys
import requests
from bs4 import BeautifulSoup
import lxml

from New_Video import New_Video
from Streams_State import Streams_State


# link = "KFHaZAIG2sA"
link = "-6JmbdjW-M0"





state = Streams_State('C:\\Users\\Vlad\\Desktop\\Data_Streams(1).txt')
print("Please wait for the result...")
x = state.get_state()
# for i in range(len(x[0])):
#     print(x[0][i])
# print("Numbers of not working links:"+x[1])

new_vid = New_Video()
for i in range(len(x[2])):
    lin = x[2][i].replace("'", '')
    res = new_vid.tst(lin)
    print(res)
