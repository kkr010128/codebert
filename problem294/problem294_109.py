import bisect
N = int(input())
L = sorted([int(i) for i in input().split()])
ans = 0

for j in range(N-2):
    for k in range(j+1,N-1):
        S = L[j] + L[k]
        a = bisect.bisect_left(L, S)
        ans += a - 1 - k 

print(ans)
