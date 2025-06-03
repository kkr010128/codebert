n=int(input())
slist=[]
tlist=[]
ans=0
yn=0
for i in range(n):
    s,t=input().split()
    slist.append(s)
    tlist.append(int(t))
x=input()
for i in range(n):
    if yn==1:
        ans+=tlist[i]
    if x==slist[i]:
        yn=1
print(ans)
