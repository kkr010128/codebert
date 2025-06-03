N = int(input())
A = list(map(int,input().split()))

import collections
B = collections.Counter(A)
count = 0
for a in B.values():
    count += (a*(a-1))//2

for a in range(N):
    D = A[a]
    print(count-B[D]+1)