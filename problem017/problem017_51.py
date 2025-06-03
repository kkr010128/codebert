# coding: utf-8
# Shell Sort 2018/3/15

def insertionSort(A, n, g):
    global cnt
    for i in range(g, n):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j+g] = A[j]
            j = j-g
            cnt += 1
        A[j+g] = v

def shellSort(A, n):
    global cnt
    cnt = 0
    if n == 1:
        G = [1]
    else:
        G = []
        h = 1
        while h < n:
            G.append(h)
            h = 3*h +1
        G = G[::-1]
    m = len(G)
    print m
    print " ".join([str(i) for i in G])
    for i in range(m):
        insertionSort(A, n, G[i])

if __name__ == "__main__":
    n = int(raw_input())
    A = []
    for i in range(n):
        A.append(int(raw_input()))
    shellSort(A, n)
    print cnt
    for i in A:
        print i

