import bisect

N = int(input())
l = list(map(int, input().split()))
l.sort()
ans = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        p = l[:i]
        a, b = l[i], l[j]
        low = b - a + 1
        high = a + b
        ans += bisect.bisect_left(p, high) - bisect.bisect_left(p, low)
print(ans)