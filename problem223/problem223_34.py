N, K = map(int, input().split())
p = list(map(int, input().split()))

# サイコロ（1...p）の期待値は(1+p)/2
cum_sum = [0]
for i in range(0, N):
    cum_sum.append(cum_sum[i] + (1 + p[i]) / 2)
# print(cum_sum)
# 調べる区間は[1,...,K],...,[N-K+1,...N]
ans = 0
for i in range(1, N - K + 2):
    temp = cum_sum[i + K - 1] - cum_sum[i - 1]
    # print(temp)
    ans = max(ans, temp)
print(ans)
