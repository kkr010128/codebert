N, K, S = map(int, input().split())

ans = [None] * N
for i in range(N):
    if i < K:
        ans[i] = S
    else:
        if S + 1 <= 1000000000:
            ans[i] = S + 1
        else:
            ans[i] = 1
            
print(' '.join(map(str, ans)))