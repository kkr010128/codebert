from collections import deque

def min_coin_select(C, m, n):
    DP = [float('inf')] * (n+1)
    DP[0] = 0
    # Cのindexが合わないので左をゼロ埋め。Cはdequeとする。
    C.appendleft(0)

    for i in range(1, m+1):
        for j in range(1, n+1):
            if j >= C[i]:
                DP[j] = min(DP[j-C[i]] + 1, DP[j])

    return DP[n]

def read_and_print_results():
    n, m = [int(i) for i in input().split()]
    C = deque([int(i) for i in input().split()])
    print(min_coin_select(C, m, n))

read_and_print_results()
