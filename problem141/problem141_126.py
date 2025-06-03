N = int(input())
A = list(map(int, input().split()))

B = []

if N == 0:
    if A[0] != 1:
        print(-1)
        exit()
    else:
        print(1)
        exit()

else:
    if A[0] != 0:
        print(-1)
        exit()
    else:
        B.append(1)
        for i in range(1, N + 1):
            B.append((B[i - 1] - A[i - 1]) * 2)
            if (A[i] > B[i] or (A[i] == B[i] and i != N)):
                print(-1)
                exit()

        ans = 0
        ans += A[N]
        B[N] = A[N]
        for i in range(N - 1, -1, -1):
            ans += min(B[i], B[i + 1] + A[i])
            B[i] = min(B[i], B[i + 1] + A[i])

        print(ans)
        exit()
