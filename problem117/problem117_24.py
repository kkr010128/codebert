def abc172c_tsundoku():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    A = [0] * (n + 1)
    B = [0] * (m + 1)

    for i in range(1, n + 1):
        A[i] = A[i - 1] + a[i - 1]
        if A[i] > k:
            n = i - 1
            break
    for i in range(1, m + 1):
        B[i] = B[i - 1] + b[i - 1]
        if B[i] > k:
            m = i - 1
            break
    ans = 0
    for i in range(0, n + 1):
        j = max(ans - i, 0)
        if j > m or A[i] + B[j] > k: continue
        while j <= m:
            if A[i] + B[j] > k:
                j -= 1
                break
            j += 1
        j = min(m,j)
        ans = max(i + j, ans)
    print(ans)


abc172c_tsundoku()