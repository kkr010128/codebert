import bisect

N = int(input())
L = list(map(int, input().split()))
L.sort()
ans = 0
for a in range(N):
    for b in range(a):
        ab = L[a] + L[b]
        r = bisect.bisect_left(L, ab)
        l = a + 1
        ans += max(r - l, 0)
print(ans)