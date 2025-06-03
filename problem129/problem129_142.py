import numpy as np

n = int(input())
a = [int(x) for x in input().split()]
a.sort()

m = np.zeros(max(a)+1, dtype=int)
cnt = 0

for i in range(n):
    x = a[i]
    if i == n-1:
        if m[x] == 0:
            cnt +=1
    else:
        if m[x] == 0 and a[i] != a[i+1]:
            cnt +=1
    m[x::x] += 1
print(cnt)