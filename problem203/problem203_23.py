a,b=map(int,input().split())
a1=a/0.08
a2=(a+1)/0.08
b1=b/0.1
b2=(b+1)/0.1
ans=20000
for i in range(1,10001):
    if a1<=i and b1<=i and a2>i and b2>i:
        ans=min(ans,i)
if ans==20000:
    print(-1)
else:
    print(ans)