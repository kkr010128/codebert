n,m,k=map(int,raw_input().split())
a=map(int,raw_input().split())
b=map(int,raw_input().split())
cnt1=0
cnt2=0
a1=[0]
b1=[0]
for i in range(n):
    a1.append(a1[-1]+a[i])
for i in range(m):
    b1.append(b1[-1]+b[i])
ans=0
j=m
for i in range(n+1):
    if a1[i]>k:
        break
    while b1[j]>k-a1[i]:
        j-=1
    ans=max(ans,i+j)
print ans