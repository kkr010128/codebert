from itertools import accumulate

N, K = map(int, input().split())
P = list(map(int, input().split()))
Q = list(map(lambda x: (x+1)/2, P))

Q_cum = list(accumulate([0] + Q))
res = 0
for i in range(N-K+1):
    temp = Q_cum[i+K]- Q_cum[i]
    res = max(res, temp)
print(res)