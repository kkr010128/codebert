cards = int(input())
i = 0
cardlist = []
while(i < cards):
    cardlist.append(list(map(str,input().split())))
    i += 1
SP = [False] * 13
HR = [False] * 13
CL = [False] * 13
DY = [False] * 13

for i in cardlist:
    num = int(i[1])-1
    if  (i[0] == "S"):
        SP[num] = True
    elif(i[0] == "H"):
        HR[num] = True
    elif(i[0] == "C"):
        CL[num] = True
    elif(i[0] == "D"):
        DY[num] = True

c = 0
for i in SP:
    c += 1
    if i == False:
        print("S %d" %c)
c = 0
for i in HR:
    c += 1
    if i == False:
        print("H %d" %c)
c = 0
for i in CL:
    c += 1
    if i == False:
        print("C %d" %c)
c = 0
for i in DY:
    c += 1
    if i == False:
        print("D %d" %c)
