n,k = map(int, input().split())

n_list=list(range(n+1))

saisyou=sum(n_list[0:k])
saidai=sum(n_list[n-k+1:n+1])

ans=saidai-saisyou+1

for i in range(k+1,n+2):
    saisyou+=n_list[i-1]
    saidai+=n_list[-(i)]
    ans+=saidai-saisyou+1
    ans%=10**9+7

print(ans)