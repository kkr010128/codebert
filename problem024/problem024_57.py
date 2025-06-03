def check(P):
 i=0
 for _ in[0]*k:
  s=0
  while s+w[i]<=P:
   s+=w[i];i+=1
   if i==n: return n
 return i
n,k=map(int,input().split())
w=[int(input())for _ in[0]*n]
l=0;r=n*100000
while r-l>1:
 m=(l+r)//2
 if check(m)>=n:r=m
 else:l=m
print(r)
