from collections import Counter
N = int(input())
Alist = list(map(int,input().split()))
numcntlist = [0] * N 
numCounter = Counter(Alist)

for i in range(1,N+1):
    numcntlist[i-1] = numCounter[i]

sumcomb = 0
for i in numcntlist:
    sumcomb += int(i*(i-1)/2)

for i in Alist:
    ans = sumcomb -(numCounter[i] - 1)
    print(ans)