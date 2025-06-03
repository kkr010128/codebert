from math import ceil,floor

A,B=map(int,input().split())
x_min=int(min(ceil(A/0.08)-5, ceil(B/0.1)-5))
x_max=int(max(ceil((A+1)/0.08)+5, ceil((B+1)/0.1)+5))
exists=0
for i in range(x_min, x_max):
  if floor(i*0.08)==A and floor(i*0.1)==B:
    print(i)
    exists=1
    break
if not exists:print(-1)