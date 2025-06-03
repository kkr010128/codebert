def solve(n, A, q, m):
    memo = dict()
    for i in range(2**n):
        tmp = 0
        for j in range(n):
            if i >> j & 1:
                tmp += A[j]
        memo[tmp] = 1

    for val in m:
        print("yes" if val in memo else "no")

if __name__ == "__main__":
    n = int(input())
    A = list(map(int, input().split()))
    q = int(input())
    m = list(map(int, input().split()))
    solve(n, A, q, m)

