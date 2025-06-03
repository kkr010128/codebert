def solve():
    N,K = map(int, input().split())
    A = list(map(int, input().split()))

    for i in range(K):

        arr = [0] * (N + 1)

        for ind,j in enumerate(A):
            arr[max(ind-j,0)] += 1
            arr[min(ind+j+1, N)] -= 1

        A[0] = arr[0]
        for k in range(N-1):
            A[k+1] = A[k] + arr[k+1]

        if arr[0] ==N and arr[-1] == -N:
            return A
    return A


if __name__ == "__main__":
    ans = solve()
    print(*ans)

