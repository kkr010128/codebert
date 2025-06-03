N=int(input())
x=list(map(int,input().split()))
sum=0
for i in range(1,N):
    if x[i]<x[i-1]:
        t=x[i-1]-x[i]
        sum+=t
        x[i]=x[i-1]
print(sum)