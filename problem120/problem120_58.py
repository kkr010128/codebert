N,K = map(int,input().split())
p_lis = list(map(int, input().split()))

sorted_lis = sorted(p_lis)

ans = 0
for i in range(K):
    ans+=sorted_lis[i]

print(ans)