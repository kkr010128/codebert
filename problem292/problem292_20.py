N=int(input())
d=list(map(int,input().split()))
l=len(d)
s=0
for i in range(l):
    for j in range(i+1,l):
        s+=d[i]*d[j]
print(s)