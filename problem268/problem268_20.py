N = int(input())
A = list(map(int, input().split()))
mod = 10**9+7
G = [0]*3
ans = 1
for i in range(N):
    x = 0
    cnt = 0
    for j, g in enumerate(G):
        if g == A[i]:
            x = j if cnt == 0 else x
            cnt += 1
    
    G[x] += 1
    ans *= cnt
    ans = ans % mod

print(ans)