def solve():
    N,K = [int(i) for i in input().split()]
    min_N = N
    if min_N > K:
        min_N = min_N - (min_N//K)*K
    min_N = min(min_N, abs(min_N-K))
    print(min_N)

if __name__ == "__main__":
    solve()