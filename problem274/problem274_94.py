# F - Sugoroku
import sys
sys.setrecursionlimit(10 ** 9)

n,m = map(int,input().split())
s = input()

# r[i]:sを後ろから見ていって、iから最小何手でゴールするかを求める。
INF = float('inf')
r = [INF for _ in range(n+1)]
r[n] = 0
idx = n
for i in range(n-1,-1,-1):
  while(idx-i > m or r[idx] == INF):
    idx -= 1
  if idx <= i:
    print(-1)
    exit()
  if s[i] == '0':
    r[i] = r[idx]+1
    p = r[i]
#print(r)

# rを先頭から見ていき、rの数字が変わる直前まで進むようにすれば
# 最短で辞書順最小なルートが求まる。
ans = []
c = 0
for i in range(n+1):
  if r[i] != INF and r[i] != p:
    p = r[i]
    ans.append(c)
    c = 1
  else:
    c += 1
print(*ans)

# mnr = [m for _ in range(n+1)]
# mnl = n+1
# def dfs(x,c):
#   global mnr,mnl
#   #print(x,c)
#   if x == n:
#     #print(r)
#     if len(r) < mnl or (len(r) == mnl and r < mnr):
#       mnr = r[:]
#       mnl = len(r)
#     return True
#   if c >= mnl or x > n or s[x] == '1':
#     return False
#   for i in range(m,0,-1):
#     r.append(i)
#     dfs(x+i,c+1)
#     r.pop()
# dfs(0,0)
# if mnl < n+1:
#   print(*mnr)
# else:
#   print(-1)