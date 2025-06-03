n = int(input())
L = []
for _ in range(n):
    L.append(int(input()))

def InsertionSort(L, n, g):  
    for i in range(n):
        global cnt
        v = L[i]
        j = i - g
        while j >= 0 and L[j] > v:
            L[j+g] = L[j]
            j -= g
            cnt += 1
        L[j+g] = v


def ShellSort(L, n):
    gt = 1
    g = []
    while n >= gt:
        g.append(gt)
        gt = 3 * gt + 1
    print(len(g))
    g = g[::-1]
    print(' '.join(str(x) for x in g))
    for x in g:
        InsertionSort(L, n, x)
    print(cnt)
    for i in L:
        print(i)

cnt = 0
ShellSort(L, n)
