N, K = map(int, input().split())
P = list(map(lambda x:int(x) - 1,input().split()))
C = list(map(int, input().split()))
ans = -10**9

for i in range(N):
    tmp_max = [-10**9]*(N+1)
    total = 0
    current_block = P[i]
    for j in range(1, N + 1):
        total += C[current_block]
        tmp_max[j] = max(tmp_max[j-1], total)
        if current_block == i:
            break
        current_block = P[current_block]
    if total <= 0:
        ans = max(ans, tmp_max[j])
    else:
        n = K // j
        r = K % j
        if r == 0:
            ans = max(ans, total*(n-1) + tmp_max[j])
        else:
            ans = max(ans, total*n + tmp_max[r])

print(ans)