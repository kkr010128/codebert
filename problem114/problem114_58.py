import copy
D = int(input())
c = list(map(int, input().split()))
s = []
for _ in range(D):
  s.append(list(map(int, input().split())))
t = []
for _ in range(D):
  t.append(int(input()))
u = [] # last(d,i)
x = [0] * 26
u.append(x)
for i in range(D):
  v = copy.deepcopy(u)
  y = v[-1]
  y[t[i]-1] = i+1
  u.append(y)
del u[0]

ans = 0
for i in range(D):
  ans += s[i][t[i]-1]
  for j in range(26):
    ans -= c[j] * ((i+1) - u[i][j]) 
  print(ans)
