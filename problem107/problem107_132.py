N = int(input())
X = input()
ans = [1 for _ in range(N)]
#original 1 count
l = X.count('1')
if l == 0:
  for _ in range(N):
    print(1)
  exit()
if l == 1:
  if X[-1] == '1':
    for _ in range(N-1):
      ans[_] = 2
  else:
    ans[-1] = 2 
  for k in range(N):
    if X[k] =='1':
      ans[k] = 0 
  for _ in range(N):
    print(ans[_])
  exit()
 
 
intN = int(X, 2)
N1 = intN %(l-1)
N0 = intN % (l+1)
 
 
start = []
if N == 1:
  if X[0] == '1':
    print(0)
    exit()
  else:
    print(1)
    exit()
else:
  s1 = 1
  s0 = 1
  for k in range(N-1, -1, -1):
    if X[k] == '1':      
      ia = (N1 - s1)%(l-1)
    else:
      ia = (N0 + s0)%(l+1)
    start.append(ia)
    s1 = s1*2%(l-1)
    s0 = s0*2%(l+1)
start = start[::-1]
 
ml = len(bin(l+1))-2
poplist = [0 for _ in range(N)]
t = 1
while t < N + 1:
  t *= 2
  for k in range(t//2, N, t):
    for j in range(t//2):
      if k+j>N-1:
        break
      poplist[k+j] += 1
"""
 
def popcount(n):
  c = 0
  n = bin(n)[2:]
  for k in range(len(n)):
    if n[k] == '1':
      c+=1
  return c
"""
for k in range(len(start)):
  for count in range(10*5):
    if start[k] == 0:
      ans[k] += count
      break
    else:
      start[k] = start[k] % poplist[start[k]]
 
for k in range(N):
  print(ans[k])