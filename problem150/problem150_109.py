n,k = map(int,input().split())
A = [0]
A.extend(list(map(int,input().split())))

town = 1
once = [0]*(n+1)

for i in range(n):
  if once[town]==0:
    once[town] = 1
  else:
    break
  town = A[town]

rt = A[town]
roop = 1
while rt != town:
  rt = A[rt]
  roop += 1

rt = 1
bf = 0
while rt != town:
  rt = A[rt]
  bf += 1  

if bf<k:
  K = (k-bf)%roop + bf
else:
  K = k

town = 1
for _ in range(K):
  town = A[town]

print(town)