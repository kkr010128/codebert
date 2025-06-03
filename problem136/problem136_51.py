N = int(input())
c = 0
b = [0]*1000
p = 0
while N % 2 == 0:
  b[p] += 1
  N //= 2
if b[p]!=0:
  p += 1
i = 3
while i * i <= N:
  if N % i == 0:
    b[p] += 1
    N //= i
  else:
    i += 2
    if b[p]!=0:
      p += 1
if N==i:
  b[p] += 1
  N //= i
if N!=1:
  p += 1
  b[p] += 1
for v in b:
  for i in range(1,v+1):
    if i<=v:
      c += 1
      v -= i
    else:
      break
print(c)