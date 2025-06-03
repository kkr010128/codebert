n=int(input())
d={}
m=1
for i in range(n):
    s=input()
    if s in d:
        d[s]+=1
        m=max(m,d[s])
    else:
        d[s]=1
se=set()
for i in d:
    if d[i]==m:
        se.add(i)
se=list(se)
se.sort()
print(*se)