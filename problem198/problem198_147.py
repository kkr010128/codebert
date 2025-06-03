import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
N = int(input())
res = set()
a = ord("a")
mx = lambda x: max(list(map(ord, x))) - a
def dfs(s):
  if len(s) == N:
    res.add("".join(s))
    return
  for k in range(mx(s) + 2): dfs(s + [chr(k + a)])
dfs(["a"])
for r in sorted(res): print(r)