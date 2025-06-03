def insertionSort(A, n, g):
    global cnt
    for i in range(g, n):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j + g] = A[j]
            j = j - g
            cnt += 1
        A[j + g] = v

def shellSort(A, n):
    global cnt
    G = []
    g = 1
    while g <= n:
        G.append(g)
        g = 3 * g + 1
    G = G[::-1]
    m = len(G)
    for i in range(m):
        insertionSort(A, n, G[i])
    return m, G, cnt, A

n = int(input())
A = []
for _ in range(n):
    A.append(int(input()))
cnt = 0
m, G, cnt, A = shellSort(A, n)
print(m)
for i in range(m):
    if i == m - 1:
        print(G[i])
    else:
        print(G[i], end=' ')
print(cnt)
for i in range(n):
    print(A[i])
