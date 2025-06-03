n,k=map(int,input().split())

#k以下のn個の数字

ans=[0]*(k+1)
p=10**9+7
result=0
for i in range(k):
    num=k-i

    ans[num]=pow(k//num,n,p)
    j=2
    while num*j<=k:
        ans[num]-=ans[num*j]
        j+=1
    result+=((ans[num]*num)%p)    
    #print(num,ans)
print(result%p)