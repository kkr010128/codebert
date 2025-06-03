d = int(input())
cList = input().split()

sList = []

for idx in range(0, d):
    tempList = input().split()
    sList.append(tempList)

tList = []

for idx in range(0, d):
    tList.append(int(input()))

countList = [0] * 26
val = 0

for idx in range(0, d):
    val += int(sList[idx][tList[idx] -1])

    countList = list(map(lambda x: x+1, countList))
    countList[int(tList[idx]) -1] = 0

    for wkChar in range(0,26):
        val -= int(countList[wkChar]) * int(cList[wkChar])
    print(val)


