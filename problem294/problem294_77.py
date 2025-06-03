import itertools, bisect

N = int(input())
L = list(map(int, input().split()))
L.sort()

ans = 0
for i in range(N):
    for j in range(i+1, N):
        cindex = bisect.bisect_left(L, int(L[i]) + int(L[j]))
        ans += cindex-1 - j

print(ans)
