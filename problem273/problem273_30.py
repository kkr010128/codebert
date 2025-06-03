from collections import defaultdict as dd
N, K = map(int, input().split())
A = list(map(int, input().split()))
S = [0]*(N+1)
# 累積和
for i in range(1, N + 1):
    S[i] = S[i - 1] + A[i - 1] - 1
    S[i] %= K
        
B = dd(int)  # ここで範囲内のS[i]-iの個数を数えていく。
cnt = 0
for j in range(1, N + 1):
    B[S[j - 1]] += 1
    if j - K >= 0:
        B[S[j - K]] -= 1
    cnt += B[S[j]]

print(cnt)