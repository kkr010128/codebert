n,k,c=map(int,input().split())
s=list(input())
p=[-1]*n
i=0
f=0
while i<n:
    if s[i]=='o':
        p[i]=f
        f+=1
        i+=c+1
    else:
        i+=1
i=0
f=0
q=[-1]*n
while i<n:
    if s[n-i-1]=='o':
        q[n-i-1]=f
        f+=1
        i+=c+1
    else:
        i+=1
for i in range(n):
    if p[i]>=0 and q[i]>=0 and p[i]+q[i]==k-1:
        print(i+1)