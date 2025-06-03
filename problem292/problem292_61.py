from itertools import accumulate
n=int(input())
d=list(map(int,input().split()))
ans=0
for i in range(n):
  ans+=(list(accumulate(d))[-1]-d[i])*d[i]
print(ans//2)