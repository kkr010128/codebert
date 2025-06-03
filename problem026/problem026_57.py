def merge(a, l, m, r):
    global cnt
    ll = a[l:m] + [1e9 + 1]
    rl = a[m:r] + [1e9 + 1]
    i, j = 0, 0
    for k in range(l, r):
        if ll[i] < rl[j]:
            a[k] = ll[i]
            i += 1
        else:
            a[k] = rl[j]
            j += 1
        cnt += 1


def merge_sort(a, l, r):
    if l + 1 < r:
        m = (l + r) // 2
        merge_sort(a, l, m)
        merge_sort(a, m, r)
        merge(a, l, m, r)


n, a, cnt = int(input()), list(map(int, input().split())), 0
merge_sort(a, 0, n)
print(*a)
print(cnt)