import time
from random import randint
d = int(input())
c = list(map(int,input().split()))
starttime = time.time()
timelimit = 1.8
ans = []
fin = [1]*d
pen = [0]*26
sattemp = 0
sat = 0
sl = [list(map(int,input().split())) for i in range(d)]
for i in range(d):
    s = sl[i]
    sp = sum(pen)
    temp = -(10**9)
    for j in range(26):
        if s[j]-(sp-pen[j]) > temp:
            temp = s[j]-(sp-pen[j])
            tempans = j+1
    ans += [tempans]
    sat += s[tempans-1]-sp+pen[tempans-1]
    for j in range(26):
        pen[j] += c[j]
        pen[tempans-1] = 0
fin = ans
ans = []
pen = [0]*26
# while time.time() - starttime <= timelimit:
#     ans = fin
#     d1 = randint(0,d-1)
#     d2 = randint(d1,min(d-1,d1+15))
#     if randint(0,1):
#         ans[d1],ans[d2] = ans[d2],ans[d1]
#         # print(1)
#     else:
#         ans[d1] = randint(1,26)
#         # print(0)
#     pen = [0]*26
#     sattemp = 0
#     for i in range(d):
#         # print(i,fin,fin[i])
#         s = sl[i]
#         sp = sum(pen)
#         tempans = ans[i]
#         sattemp += s[tempans-1]-sp+pen[tempans-1]
#         for j in range(26):
#             pen[j] += c[j]
#             pen[tempans-1] = 0
#         # print(sattemp)
#     if sattemp > sat:
#         fin = ans
#         sat = sattemp
#         # print(sat)
for i in fin:
    print(i)
# print(sat)

