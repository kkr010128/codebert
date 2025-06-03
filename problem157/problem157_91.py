from collections import defaultdict
N = int(input())
A = [int(i) for i in input().split()]

ans = 0
d = defaultdict(int)
cur = N
for a in A[::-1]:
    ans += d[cur + a]
    if cur - a > 0:
        d[cur - a] += 1
    cur -= 1
print(ans)