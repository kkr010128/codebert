a,b,c,k=map(int,input().split())
ans=a
if a>k: ans=k
if a+b<k: ans-=(k-(a+b))
print(ans)
