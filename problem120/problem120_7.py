n,k=map(int,input().split())
p=list(map(int,input().split()))
sw=0
sum=0
for i in range(n):
    for j in range(n-1):
        if p[j]>=p[j+1]:
            sw=p[j]
            p[j]=p[j+1]
            p[j+1]=sw
for i in range(k):
    sum+=p[i]
print(sum)