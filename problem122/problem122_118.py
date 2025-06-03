n=int(input())
a=list(map(int,input().split()))
q=int(input())
bc=[list(map(int,input().split())) for i in range(q)]
d=[0 for i in range(pow(10,5)+1)]
s=sum(a)
for i in range(n):
    d[a[i]]+=1
for i in range(q):
    s+=(bc[i][1]-bc[i][0])*d[bc[i][0]]
    print(s)
    d[bc[i][1]]+=d[bc[i][0]]
    d[bc[i][0]]=0
