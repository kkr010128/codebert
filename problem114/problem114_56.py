d=int(input())
a=[0 for i in range(26)]
c=list(map(int,input().split()))
l=[]
for i in range(d):
    l.append(list(map(int,input().split())))
    #print(c.index(max(c))+1)
p=[0]
for i in range(1,d+1):
    t=int(input())-1
    a[t]=i
    k=0
    for j in range(26):
        k+=c[j]*(i-a[j])
    p.append(p[i-1]+l[i-1][t]-k)
print(*p[1:],sep='\n')