from New_Video import New_Video
from Streams_State import Streams_State

state = Streams_State('C:\\Users\\Vlad\\Desktop\\Data_Streams(1).txt')
print("Please wait for the result...")

#запрашиваем статус трансляций и повторы
x = state.get_state()
print("\nLink status:\n")

#выводим состояние трансляций
for i in range(len(x[0])):
    print(x[0][i])

print("\nReplacements:\n")

#выводим замены
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

#выводим повторы
for i in x[3]:
    if x[3][i].count(",") > 1:
        print(i, ":", x[3][i])
