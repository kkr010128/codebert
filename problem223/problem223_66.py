N, K = map(int, input().split())
plist = list(map(int, input().split()))

pre = sum(plist[:K])
ans = pre
for i in range(0, N-K):
    pre = pre - plist[i] + plist[i+K]
    ans = max(ans, pre)

print((ans + K)/2)
