N, K = map(int, input().split())
H = list(map(int, input().split()))

if N <= K:
    print(0)
else:
    H = sorted(H)
    ans = 0
    for i in range(N-K):
        ans += H[i]
    print(ans)