a1 = list(map(int,input().split()))
a2 = list(map(int,input().split()))
a3 = list(map(int,input().split()))

ans = "No"

n = int(input())

for i in range(n):
    p = int(input())
    if a1.count(p)>0:
        a1[a1.index(p)]=-1
    if a2.count(p)>0:
        a2[a2.index(p)]=-1
    if a3.count(p)>0:
        a3[a3.index(p)]=-1

if max(a1)==-1 or max(a2)==-1 or max(a3)==-1:
    ans="Yes"

if (a1[0]==-1 and a2[0]==-1 and a3[0]==-1) or (a1[1]==-1 and a2[1]==-1 and a3[1]==-1) or ((a1[2]==-1 and a2[2]==-1 and a3[2]==-1)):
    ans="Yes"

if (a1[0]==-1 and a2[1]==-1 and a3[2]==-1) or (a1[2]==-1 and a2[1]==-1 and a3[0]==-1) :
    ans="Yes"

print(ans)

