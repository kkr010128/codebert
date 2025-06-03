N, K = map(int, input().split())
ppp = list(map(int, input().split()))
acc = 0
for i in range(K):
    acc +=  (ppp[i] + 1) / 2
ans = acc
for i in range(K, N):
    acc -= (ppp[i - K] + 1) / 2
    acc += (ppp[i] + 1 ) / 2
    ans = max(ans, acc)
print(ans)
