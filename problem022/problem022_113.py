n = list(input())
sList = list(map(int,input().split()))

q = list(input())
tList = list(map(int,input().split()))

tCount = 0


for tmp_t in tList:
    if 0 < sList.count(tmp_t):
        tCount += 1

print(tCount)