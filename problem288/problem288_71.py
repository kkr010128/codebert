n=int(input())
a=1
ans=n
while a*a<=n:
    if n%a==0:
        ans=min(a+n//a-2,ans)
    a+=1
print(ans)