v, e = map(int,input().split())
par = [i for i in range(v+1)]

def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return 0
    par[x] = y

for i in range(e):
  a, b = map(int, input().split())
  unite(a, b)
  
cnt = 0
for i in range(v+1):
  if i == par[i]:
    cnt += 1

print(cnt-2)