INF = 10**9 + 1
cnt = 0


def merge(A, left, mid, right):
    global INF, cnt
    L = []
    R = []
    for i in range(left, mid):
        L.append(A[i])
    L.append(INF)
    for i in range(mid, right):
        R.append(A[i])
    R.append(INF)

    i = 0
    j = 0
    for k in range(left, right):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        cnt += 1


def merge_sort(A, left, right):
    # range: [left, right)
    if right - left <= 1:
        return
    mid = (left + right) / 2
    merge_sort(A, left, mid)
    merge_sort(A, mid, right)
    merge(A, left, mid, right)


if __name__ == '__main__':
    n = int(raw_input())
    A = map(int, raw_input().split())
    merge_sort(A, 0, n)
    for x in A:
        print x,
    print
    print cnt
