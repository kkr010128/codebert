N,K,C= map(int,input().split())
S = input()

dp = [0]*(N+1)
dpr = [0]*(N+1)
for i in range(1,N+1):
    if S[i-1] == 'o':
        p = max(i-C-1,0)
        if dp[i-1] < dp[p] + 1:
            dp[i] = dp[p] + 1
            dpr[i] = i + C
            continue
    dp[i] = dp[i-1]
    dpr[i] = dpr[i-1]

rdp = [0]*(N+2)

for i in range(N,-1,-1):
    if S[i-1] == 'o':
        rdp[i] = max(rdp[i+1],rdp[min(N+1,i+C+1)]+1)
    else:
        rdp[i] = rdp[i+1]

ans = []
for i in range(1,N+1):
    if dp[i-1] + rdp[max(i+1,min(dpr[i-1]+1,N+1))] < K:
        ans.append(i)

for a in ans:
    print(a)

    



