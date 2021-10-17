import sys
import requests
from bs4 import BeautifulSoup
import lxml

from New_Video import New_Video
from Streams_State import Streams_State
# link = "KFHaZAIG2sA"

state = Streams_State('C:\\Users\\Vlad\\Desktop\\Data_Streams(1).txt')
print("Please wait for the result...")

x = state.get_state()
print("\nLink status:\n")
# print(x)
for i in range(len(x[0])):
    print(x[0][i])
## print("Numbers of not working links:"+x[1])

print("\nReplacements:\n")
if len(x[2]) == 0: print("No links needing replacement\n")
new_vid = New_Video()
for i in range(len(x[2])):
    try:
        lin = x[2][i].replace("'", '')

        r1 = new_vid.tst(lin)
        answer = x[1][i] +  " - " + r1
        print(answer)
    except:
        print(x[1][i]+": "+"We could not find a replacement for this video")
        # print("Error: "+ str(sys.exc_info()[1]))

print("\nRepeated:\n")
for i in x[3]:
    if x[3][i].count(",") > 1:
        print(i, ":", x[3][i])
