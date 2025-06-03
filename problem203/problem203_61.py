import math
A, B = list(map(int, input().split()))
ans = -1
low = math.floor(min(A//0.08, B//0.1))
hig = math.ceil(max((A+1)//0.08, (B+1)//0.1))
for i in range(low, hig):
   a = math.floor(i * 0.08)
   b = math.floor(i * 0.1)
   if A == a and B == b:
     ans = i
     break
print(ans)