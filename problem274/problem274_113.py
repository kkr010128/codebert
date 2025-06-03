n,m=map(int,input().split())
s=input()
res=[]
now=n
while now!=0:
    j=False
    for i in range(max(0,now-m),now):
        if s[i]=="0":
            j=True
            res.append(now-i)
            now=i
            
            break
    if not j:
        print(-1)
        exit()
for i in range(len(res)-1,-1,-1):
    print(res[i],end=" ")