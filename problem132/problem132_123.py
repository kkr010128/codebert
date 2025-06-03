def draft(A, K, N):
    for _ in range(1, K+1):# 2 * 10**5
        tmp = [0]*(N+1)
        for i in range(N):# 2 * 10**5
            L = max(0, i - A[i])
            R = min(N, i + A[i]+1)
            tmp[L] += 1
            tmp[R] -= 1
        f = True
        for i in range(N):
            tmp[i+1] += tmp[i]
            A[i] = tmp[i]
            if A[i] != N:
                f = False
        if f:
            break
    for i in range(N):
        print(A[i], end=" ")

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    draft(A, K, N)

if __name__ == "__main__":
    main()
