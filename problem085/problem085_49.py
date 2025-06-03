import math

n = int(input())
a = list(map(int,input().split()))

MAX = 1000005

is_prime = [1]*MAX
D = [None]*MAX
is_prime[0],is_prime[1] = 0,0

for i in range(2,MAX):
  if is_prime[i]:
    D[i] = i
    for j in range(i*2,MAX,i):
      is_prime[j] = 0
      D[j] = i
      
counts = [0]*MAX
pair = True

for a_i in a:
  if a_i == 1:
    continue
  pf = {}
  while True:
    p = D[a_i]
    if counts[p]>0:
      pair = False
    pf[p] = pf.get(p,0)+1
    if p == a_i:
      break
    else:
      a_i //= p
      
  for p in pf.keys():
    counts[p] += 1

if pair:
  print('pairwise coprime')
else:
  g = a_i
  for a_i in a:
    g = math.gcd(a_i,g)
  if g == 1:
    print('setwise coprime')
  else:
    print('not coprime')