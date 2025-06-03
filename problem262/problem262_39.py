from itertools import product

N=int(input())
datas=[]
for i in range(N):
    A=int(input())
    for j in range(A):
        x,y=map(int,input().split())
        datas.append((i,x-1,y)) #誰が　誰に　どう判断した？

#print(datas)

ans=0
for i in product([0,1],repeat=N):
    ok=True
    for j in datas:
        if i[j[0]]==1 and i[j[1]]!=j[2]:
            ok=False
            break
    if ok:
        ans=max(ans,sum(i))
print(ans)