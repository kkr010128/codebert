n,m=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(m)]
for i in range(1001):
    i=str(i)
    if len(i)!=n:
        continue
    f=1
    for s,c in l:
        c=str(c)
        if len(i)<s:
            f=0
            break
        if not i[s-1]==c:
            f=0
            break
    if f:
        print(i)
        exit()
print("-1")