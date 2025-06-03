n=int(input())
ans=100000

for i in range(n):
    ans+=ans*0.05
    if ans%1000!=0:
        ans-=ans%1000
        ans+=1000
    ans=int(ans)
print(ans)
