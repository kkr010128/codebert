n,k=map(int,input().split())
h=list(map(int,input().split()))
sum=0
for l in h:
    if l>=k:
        sum+=1

print(sum)