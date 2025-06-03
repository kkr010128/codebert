N, K = map(int, input().split())
P = list(map(int, input().split()))

S = [0]
sum_ = 0
for i, p in enumerate(P):
  sum_ += p
  S.append(sum_)


max_sum = 0
for i in range(N-K+1):
  max_sum = max(max_sum, S[i+K] - S[i])

res = (max_sum + K) / 2

print(res)