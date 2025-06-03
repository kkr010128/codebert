N = int(input())
A = [0 for k in range(int(N**0.5)+1)]

#N=1の処理
if N == 1:
  print(0)
  exit()
ans = 0


prime = [2]
for k in range(3, len(A), 2):
  if A[k] == 0:
    prime.append(k)
    for j in range(k, len(A), k):
      A[j] = 1
for p in prime:
  if N%p == 0:
    break
else: 
  print(1)
  exit()

used = []
use = []
#print(prime)
for p in prime:
  if p > N:
    break
  if N%p == 0:
    #print(p)
    ans += 1
    used.append(p)
    use.append(p)
    N = N // p
  np = p * p
  while N % np == 0:
    #print(np)
    ans += 1
    used.append(np)
    N = N // np
    np = np * p
    
#print(use)
#print(N)

for u in used:
  if N % u == 0:
    N = N // u
for u in used:
  if N % u == 0:
    N = N // u
for u in used:
  if N % u == 0:
    N = N // u
if N > 1:
  ans += 1
print(ans)    