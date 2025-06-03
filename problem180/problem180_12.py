def solve():
    N, K = list(map(int, input().split()))
    if(N >= K):
        tmp = N - ((N // K) * K)
        ans = min(tmp, abs(abs(tmp) - K))
    elif(N < K):
        if(K <= 2*N):
            ans = abs(N - K)
        else:
            ans = abs(N)
    print(ans)

if __name__ == "__main__":
    solve()