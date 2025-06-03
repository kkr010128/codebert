n,m,x=map(int,input().split())
A=[list(map(int,input().split())) for _ in range(n)]
a=[]
ans=[]
for i in range(2**n):
    b=bin(i)[2:].zfill(n)
    a.append(b)
for bit in a:
    Skills=[]
    for i in range(1,1+m):
        skill=0
        for j in range(n):
            if bit[j]=="1":
               skill+=A[j][i]
        Skills.append(skill)
    cost=0
    if min(Skills)>=x:
        for j in range(n):
            if bit[j]=="1":
                cost+=A[j][0]
        ans.append(cost)
if len(ans)==0:
    ans.append(-1)
print(min(ans))