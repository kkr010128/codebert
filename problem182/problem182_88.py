INF = float("inf")
n, k, c = map(int, input().split())
s = input()
l, r = [(0, -INF)] + [None] * n, [(0, INF)] + [None] * n
for i, x in enumerate(s):
    wn, wd = l[i]
    l[i+1] = (wn+1, i) if x == "o" and i-wd > c else l[i]

for i, x in enumerate(s[::-1]):
    wn, wd = r[i]
    j = n-i-1
    r[i+1] = (wn+1, j) if x == "o" and wd-j > c else r[i]

for i in range(n):
    ln, ld = l[i]
    rn, rd = r[n-i-1]
    w = ln + rn
    if rd - ld <= c: w -= 1
    if w < k: print(i+1)
