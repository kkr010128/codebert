import sys
mapin = lambda: map(int, sys.stdin.readline().split())
listin = lambda: list(map(int, sys.stdin.readline().split()))
inp = lambda: sys.stdin.readline()

N = int(inp())
mp = {}
for i in range(N):
    S = inp()
    S = S[:-1]
    if S in mp:
        mp[S] += 1
    else:
        mp[S] = 1
ans = 0
vec = []
for i in mp.values():
    if ans < i:
        ans = i
for i in mp.keys():
    if mp[i] == ans:
        vec.append(i)
vec.sort()
for i in vec:
    print(i)