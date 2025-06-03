def insertionSort(n, A, g):
    global cnt
    for i in range(g, n):
        temp = A[i]
        j = i - g
        while j >= 0 and A[j] > temp:
            A[j + g] = A[j]
            j -= g
            cnt += 1
        A[j + g] = temp
    return A


def shellSort(A, n):
    global m
    global G

    h = 1
    while True:
        if h > n:
            break
        G.append(h)
        h = 3 * h + 1
    G.reverse()
    m =len(G)

    for i in range(m):
        insertionSort(n, A, G[i])


if __name__ == "__main__":
    n = int(input())
    A = [int(input()) for i in range(n)]
    G = []
    m = 0
    cnt = 0
    shellSort(A, n)
    print(m)
    print(*G)
    print(cnt)
    for i in range(n):
        print(A[i])