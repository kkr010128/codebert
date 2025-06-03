n, k = [int(_) for _ in input().split()]
ary = [int(input()) for _ in range(n)]


def search_v(p):
    v = 0
    w = 0
    tmp_k = 1
    ind = 0

    while True:

        if tmp_k > k:
            return v
        if ind == n:
            return n

        tmp = ary[ind]
        if w + tmp <= p:
            w += tmp
            v += 1
            ind += 1
        else:
            w = 0
            tmp_k += 1


max_p = n * 10000
ps = range(max_p + 1)
left = 0
right = max_p

while left + 1 < right:
    mid = (left + right) // 2
    v = search_v(ps[mid])

    if v >= n:
        right = mid
    else:
        left = mid

print(ps[right])

