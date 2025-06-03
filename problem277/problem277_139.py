h,w,k=map(int,input().split())
cnt=1
ss=[input() for i in range(h)]
ans=[[0 for i in range(w)]for f in range(h)]
misyori=0
for ok in range(h):
    s=ss[ok]
    if set(s)!=set("."):
        v=[gg for gg in range(w) if s[gg]=="#"]
        l=[0]*w
        for k in v[:-1]:
            l[k+1]=1
        l[0]=cnt
        for i in range(1,w):
            l[i]+=l[i-1]
        for tate in range(misyori,ok+1):
            ans[tate]=l
        misyori=ok+1
        cnt+=len(v)
for t in range(misyori,h):
    ans[t]=l
for i in range(h):
    print(*ans[i],sep=" ")