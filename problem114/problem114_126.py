import sys
stdin = sys.stdin
sys.setrecursionlimit(10**6)
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
nn = lambda: list(stdin.readline().split())
ns = lambda: stdin.readline().rstrip()

d = ni()
c = na()
s = []

for i in range(d):
    ss = na()
    s.append(ss)

last = [0]*26
score = 0

for i in range(1,d+1): # i日目
    t = ni()
    t-=1 # 0-index
    last[t] = i
    score += s[i-1][t]
    for j in range(26):
        score -= c[j]*(i-last[j])
    print(score)


score = max(10**6+score, 0)