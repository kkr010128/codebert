MOD = 10**9 + 7
N, K = map(int, input().split())
A = sorted([int(i) for i in input().split()])

B = []
plus, zero, minus = 0, 0, 0
for i in range(N):
    if A[i] >= 0:
        B.append((A[i], 1))
        plus += 1
    elif A[i] == 0:
        B.append((0, 0))
        zero += 1
    else:
        B.append((-A[i], -1))
        minus += 1


if plus >= K-(min(K, minus)//2*2):
    B = sorted(B, key=lambda x: x[0], reverse=True)

    c = 1
    for i in range(K):
        c *= B[i][1]

    if c == 1:
        ans = 1
        for i in range(K):
            ans *= B[i][0]
            ans %= MOD

    else:
        ap, an = 1, 1
        skip = []
        for i in range(K-1, -1, -1):
            if B[i][1] == 1:
                ap *= B[i][0]
                skip.append(i)
                break
        else:
            skip.append(K-1)
            an = 0
        for i in range(K-1, -1, -1):
            if B[i][1] == -1:
                an *= B[i][0]
                skip.append(i)
                break
        else:
            skip.append(K-1)
            ap = 0
        for i in range(K, N):
            if B[i][1] == 1:
                ap *= B[i][0]
                break
        for i in range(K, N):
            if B[i][1] == -1:
                an *= B[i][0]
                break
        a = max(ap, an)

        ans = 1
        for i in range(K):
            if i not in skip:
                ans *= B[i][0]
                ans %= MOD
        ans *= a
        ans %= MOD

elif zero >= K-(min(K, minus)//2*2):
    print(0)
    exit()

else:
    B = sorted(B, key=lambda x: x[0], reverse=False)
    ans = 1
    for i in range(K):
        ans *= B[i][0]*B[i][1]
        ans %= MOD

print(ans)
