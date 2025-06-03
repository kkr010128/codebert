n = int(input())
strList = []
timeList = []
for x in range(n):
    s, t = map(str, input().split())
    strList.append(s)
    timeList.append(int(t))
x = input()
id = strList.index(x)
if timeList.count == id: print(0)
else: print(sum(timeList[id + 1:]))