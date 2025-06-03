from collections import Counter
N = int(input())
A = list(map(int, input().split()))
L = dict(Counter([i+A[i] for i in range(N)]))
R = dict(Counter([i-A[i] for i in range(N)]))
cnt = 0
for x in L:
    cnt += L[x]*R.get(x, 0)
print(cnt)