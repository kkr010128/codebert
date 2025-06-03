import bisect
n = int(input())
l = list(map(int, input().split()))

l.sort()

ans = 0
for a in range(0, n-2):
    for b in range(a+1, n-1):
        c = l[a] + l[b]
        ans += bisect.bisect_left(l, c) - b - 1

print(ans)