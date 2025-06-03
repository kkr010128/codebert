import sys
input = sys.stdin.readline

n = int(input())
L = [int(x) for x in input().split()]
cnt = 0

def Merge(S, l, m, r):
    global cnt
    cnt += r - l
    L = S[l:m] + [float('inf')]
    R = S[m:r] + [float('inf')]
    i, j = 0, 0
    for k in range(l, r):
        if L[i] < R[j]:
            S[k] = L[i]
            i += 1
        else:
            S[k] = R[j]
            j += 1
    return

def MergeSort(S, l, r):
    if r - l > 1:
        m = (l + r) // 2
        MergeSort(S, l, m)
        MergeSort(S, m, r)
        Merge(S, l, m, r)
    return

MergeSort(L, 0, n)
print(*L)
print(cnt)
