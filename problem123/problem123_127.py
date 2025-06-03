def resolve():
    N = int(input())
    A = list(map(int, input().split()))
    B = A[0]
    for i in range(1, N):
        B = B^A[i]
    ans = []
    for i in range(N):
        ans.append(B^A[i])
    print(*ans)

if __name__ == "__main__":
    resolve()

