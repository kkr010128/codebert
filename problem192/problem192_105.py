from collections import Counter
from math import factorial
N = int(input())
A = list(map(int, input().split()))
Acount = Counter(A)
Chose = {}
total = 0
for k, v in Acount.items():
    if Acount[k] >= 2:
        x = int(v*(v-1)/2)
        Chose[k] = x
    else:
        x = 0
        Chose[k] = x
    total = total+x
for i in range(N):
    ans=total-Chose[A[i]]
    if Acount[A[i]]-1>=2:
        ans=ans+(Acount[A[i]]-1)*(Acount[A[i]]-2)/2
    print(int(ans))
