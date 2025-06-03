import sys
N = int(sys.stdin.readline().rstrip())
sec = []

for _ in range(N):
    x, l = map(int, sys.stdin.readline().rstrip().split())
    sec.append((x - l, x + l))

sec = sorted(sec, key=lambda x: x[1])
r = -float("inf")
ans = 0
for s, t in sec:
    if r <= s:
        ans += 1
        r = t
print(ans)