N = int(input())
L = sorted([int(i) for i in input().split()])
count = 0

from bisect import bisect_left as bi

for j in range(N):
    for k in range(j + 1,N - 1):
        right = L[j] + L[k]
        ite_right = bi(L,right)
        count = count + (ite_right - k - 1)

print(count) 