from collections import Counter

n=int(input())
A=list(map(int,input().split()))

c=Counter(A)
s=0
for v in c.values():
  s+=v*(v-1)//2
for i in range(n):
  ans=s-(c[A[i]])+1
  print(ans)