import bisect

N = int(input())
L = list(map(int, input().split()))
L.sort()

ans = 0

for i in range(N - 1, 1, -1):
    for j in range(i - 1, 0, -1):
        x = bisect.bisect(L, L[i] - L[j])
        ans += max((j - x), 0)

print(ans)
