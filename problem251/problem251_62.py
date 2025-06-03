#abc149-d
n,k=map(int,input().split())
s,p,r=map(int,input().split())
f={'s':s,'p':p,'r':r}
t=str(input())
ans=0
for i in range(k):
    a=i+k
    last=t[i]
    ans+=f[last]
    while a<n-k:
        if t[a]==last:
            if t[a+k]==last:
                if last=='s':
                    last='r'
                else:
                    last='s'
            else:
                if last=='s':
                    if t[a+k]=='r':
                        last='p'
                    else:
                        last='r'
                elif last=='r':
                    if t[a+k]=='s':
                        last='p'
                    else:
                        last='s'
                else:
                    if t[a+k]=='r':
                        last='s'
                    else:
                        last='r'
        else:
            last=t[a]
            ans+=f[last]
        a+=k
    
    if a<n:
        if t[a]!=last:
            ans+=f[t[a]]

print(ans)