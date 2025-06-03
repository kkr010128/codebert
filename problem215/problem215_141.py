if __name__ == "__main__":
    n, k = map(int, input().split())
    p = 10**9 + 7

    answer = 0
    nCi = 1
    n_1Ci = 1
    for i in range(min(k + 1, n)):
        answer += nCi * n_1Ci
        answer %= p
        deno = pow(i + 1, p - 2, p)
        nCi *= (n - i) * deno
        nCi %= p
        n_1Ci *= (n - i - 1) * deno
        n_1Ci %= p

    print(answer)
