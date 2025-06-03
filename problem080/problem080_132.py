# Fast IO (be careful about bytestring, not on interactive)

import os,io
input=io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

N = int(input())

sumList = []
subList = []

for _ in range(N):
    x,y = map(int,input().split())
    sumList.append(x + y)
    subList.append(x - y)

print(max(max(sumList) - min(sumList),max(subList) - min(subList)))