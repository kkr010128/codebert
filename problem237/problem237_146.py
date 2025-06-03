import sys
N = int(sys.stdin.readline().rstrip())
sec = []

for _ in range(N):
    x, l = map(int, sys.stdin.readline().rstrip().split())
    sec.append((x - l + 1, x + l - 1))

sec = sorted(sec, key=lambda x: x[1])
r = -10**10
ans = 0
for s, t in sec:
    if r + 1 < s:
        ans += 1
        r = t
print(ans)