N = int(input())
import math

ans = []

for i in range(1,round((N-1)**0.5)+1):
  if (N-1)%i == 0:
    ans.append(i)
    if (N-1)//i != i:
      ans.append((N-1)//i)

ans.remove(1)
ans.append(N)
for i in range(2,round(N**0.5)+1):
  if N%i == 0:
    n = N
    while n%i==0:
      n//=i
    if n%i==1:
      ans.append(i)

print(len(ans))
