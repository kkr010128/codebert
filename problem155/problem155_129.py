n,m = map(int,input().split())
h = list(map(int,input().split()))
r = ['t'] * n
for i in range(m):
  x,y = map(int,input().split())
  if h[x-1] > h[y-1]:
    r[y-1] = 'f'
  elif h[x-1] < h[y-1]:
    r[x-1] = 'f'
  else:
    r[y-1] = 'f'
    r[x-1] = 'f'
    
s = 0
for i in range(n):
  if r[i] == 't':
    s += 1
    
print(s)    