n,m=map(int,input().split())
pp=[0]*n
res=0

qq=[True]*n
for i in range(m):
    i,j=input().split()
    i=int(i)
    i-=1
    if j=="AC":
        if qq[i]:
            qq[i]=False
            res+=pp[i]
    else:
        pp[i]+=1

print(qq.count(False),res)