N = int(input())
A = list(map(int,input().split()))
from collections import Counter
ctr = Counter(A)
tmp = sum(v*(v-1)//2 for v in ctr.values())
for a in A:
    print(tmp - ctr[a] + 1)