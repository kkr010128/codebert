n=int(input())
a=list(map(int,input().split()))
tot=sum(a)
b=0
c=10**10
d=0
for i in range(n):
  b+=a[i]
  d=abs(tot/2 - b)
  if d<c:
    c=d
print(int(2*c))