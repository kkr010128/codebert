S = list(input())
K = int(input())


def solve(S, K):
    T = S * K
    ans = 0
    for i in range(len(T) - 1):
        if T[i] == T[i + 1]:
            ans += 1
            T[i + 1] = "*"
    return ans


A = [solve(S, i) for i in range(6)]
if K <= 5:
    print(A[K])
else:
    if K % 2 == 1:
        d = A[5] - A[3]
        print(A[5] + (K - 5) // 2 * d)
    else:
        d = A[4] - A[2]
        print(A[4] + (K - 4) // 2 * d)
