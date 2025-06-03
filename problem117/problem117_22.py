n,m,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

b2=[]
b2.append(0)
for i in range(1,m+1):
  b2.append(b2[i-1]+b[i-1])
a.insert(0,0)
cnt=0
a_sum=0
for i in range(n+1):
  j=m
  a_sum+=a[i]
  while True:
    if k>=a_sum+b2[j]:
      cnt=max(cnt,i+j)
      m=j
      break
    j-=1
    if j <0:
      break
print(cnt)