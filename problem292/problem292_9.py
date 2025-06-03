N=int(input())
d=list(map(int,input().split()))
a=0
for i in range(len(d)):
    for j in range(len(d)):
        if i!=j and i>j:
            a+=d[i]*d[j]
print(a)