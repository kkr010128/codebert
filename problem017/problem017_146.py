def insertionSort(A, n, g):
    local_cnt = 0
    for i in range(g, n):
        # print(i, local_cnt)
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            # print(i, j, local_cnt)
            A[j + g] = A[j]
            j -= g
            local_cnt += 1
        A[j + g] = v
    return A, local_cnt

def shellSort(A, n):
    cnt = 0
    m = 1
    G = []
    
    h = 1
    while (h < n // 3):
        h = h * 3 + 1
        m += 1

    # print(f'm: {m}')

    while True:
        G.append(h)
        if h == 1:
            break
        h //= 3

    # print(f'G: {G}')
    
    for i in range(m):
        ans = insertionSort(A, n, G[i])
        # print(ans)
        A = ans[0]
        cnt += ans[1]

    return m, G, A, cnt


n = int(input())
A = [int(input()) for _ in range(n)]

m, G, A, cnt = shellSort(A, n)

print(m)
print(' '.join(str(g) for g in G))
print(cnt)
for a in A:
    print(a)
