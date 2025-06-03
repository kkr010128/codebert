from sys import stdin
import collections
def ip(): return [int(i) for i in stdin.readline().split()]
def sp(): return [str(i) for i in stdin.readline().split()]

# 4 6
# 1 2
# 1 3
# 1 4
# 2 3
# 2 4
# 3 4

def find(d,x):
    root = x
    while root != d[root]:
        root = d[root]

    while x != root:
        nxt = d[x]
        d[x] = root
        x = nxt
    return d,root


def merge(d,s,x,y):
    d,x = find(d,x)
    d,y = find(d,y)
    if x == y: return d,s
    if s[x] > s[y]:
        s[x] += s[y]
        d[y] = d[x]
    else:
        s[y] += s[x]
        d[x] = d[y]
    return d,s


n,m = ip()
d = {i+1: i+1 for i in range(n)}
s = {i+1: 1 for i in range(n)}
seen = set()
for _ in range(m):
    # print(d,s)
    x,y = ip()
    if (x,y) in seen or (y,x) in seen: continue
    seen.add((x,y))
    seen.add((y,x))
    d,s = merge(d,s,x,y)
ans = 0
for i in s:
    ans = max(ans, s[i])
print(ans)
