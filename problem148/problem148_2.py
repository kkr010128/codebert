a,b,c,k= map(int,input().split())
ans=a
if k<a:
    ans = k
if a+b<k:
    ans = ans-k+a+b

print(ans)