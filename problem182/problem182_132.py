import sys

stdin = sys.stdin

ns = lambda: stdin.readline().rstrip()
ni = lambda: int(stdin.readline().rstrip())
nm = lambda: map(int, stdin.readline().split())
nl = lambda: list(map(int, stdin.readline().split()))

n, k, c = nm()
s = ns()
g = [0]*n
f = [0]*n
_h = 0
for i in reversed(range(n)):
    if i + c + 1 < n:
        if _h < g[i+c+1]:
            _h = g[i+c+1]
    if s[i] == 'o':
        g[i] = _h + 1
if max(g) == k:
    _h = 0
    for i in range(n):
        if i > c:
            if _h < f[i-c-1]: _h = f[i-c-1]
        if s[i] == 'o':
            f[i] = _h + 1
    # print(g)
    # print(f)
    a = [0]*(k+2)
    b = [0]*(k+2)
    for i in range(n):
        a[g[i]] = i
    for i in reversed(range(n)):
        b[k+1-f[i]] = i
    # print(a)
    # print(b)
    for i in range(k, 0, -1):
        if a[i] == b[i]:
            print(a[i] + 1)