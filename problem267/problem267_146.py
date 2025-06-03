n=int(input())
s=list(input())
fa=[n+1]*10
la=[-1]*10
for i in range(n):
    s[i]=int(s[i])
    if fa[s[i]]>n:
        fa[s[i]]=i
    la[s[i]]=i
ans=0
for i in range(10):
    for j in range(10):
        if fa[i]<la[j]:
            num=[0]*10
            for k in range(fa[i]+1,la[j]):
                num[s[k]]=1
            ans+=num.count(1)
print(ans)
