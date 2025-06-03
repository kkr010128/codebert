import numpy as np

def seachPrimeNum(N):
    max = int(np.sqrt(N))
    seachList = [i for i in range(2,N+1)]
    primeNum = []
    while seachList[0] <= max:
        primeNum.append(seachList[0])
        tmp = seachList[0]
        seachList = [i for i in seachList if i % tmp != 0]
    primeNum.extend(seachList)
    return primeNum

X = int(input())
primeNum = seachPrimeNum(100003)
i = 0
while True:
    if primeNum[i] >= X:
        ans = primeNum[i]
        break
    else:
        i += 1

print(ans)
