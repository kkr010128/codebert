N, M = map(int, input().split())
ac = 0
pena = 0
count = [0 for _ in range(N+1)]
for _ in range(M):
  p, S = input().split()
  p = int(p)
  if S == 'AC':
    if count[p] > -1:
      pena += count[p]
      ac += 1
    count[p] = -10**5-1
  else:
    count[p] += 1
  
print(ac, pena)
  
