from itertools import product
datas=[]
num=0

N=int(input())
for i in range(N):
    a=int(input())
    for j in range(a):
        x,y=map(int,input().split())
        datas.append((num,x-1,y))
    num+=1
#print(datas)

ans=0
for i in product([0,1],repeat=N):
    ok=True
    cnt=0
    for j in datas:
        if (i[j[0]]==1 and i[j[1]]!=j[-1]):
            ok=False
            break
    if ok:
        cnt=sum(i)
        ans=max(ans,cnt)
    
print(ans)