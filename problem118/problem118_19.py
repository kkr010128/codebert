N = int(input())
memo = [1]*(N+1)
for i in range(2,N+1):
    tmp = i
    while tmp <= N:
        memo[tmp] += 1
        tmp += i
ans = 0
for key,val in enumerate(memo):
    ans += key*val
print(ans)