
def InsertionSort(A, n, g):
    cnt = 0

    for i in range(g, n):
        v = A[i]
        j = i - g

        while j >= 0 and A[j] > v:
            A[j + g] = A[j]
            j -= g
            cnt += 1

        A[j + g] = v

    return cnt

def ShellSort(A, n):
    total_cnt = 0

    G = [1]
    span = 4

    while span < len(A):
        G.append(span)
        span = span * 3 + 1

    G.reverse()

    m = len(G)

    for i in range(m):
        total_cnt += InsertionSort(A, n, G[i])

    return m, G, total_cnt

n = int(input())
A = []

for i in range(n):
    A.append(int(input()))

m, G, cnt = ShellSort(A, n)

print(m)
print(*G)
print(cnt)

for a in A:
    print(a)