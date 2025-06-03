
def f(w, n, k, v):
    # how many things in list w of length n can fill in k cars with capacity v?
    i = 0
    space = 0
    while i < n:
        if space >= w[i]:
            space -= w[i]
            i += 1
        else:
            # space < w[i]
            if k == 0:
                break
            k -= 1
            space = v
    return i


if __name__ == '__main__':
    n, k = map(int, raw_input().split())
    w = []
    maxv = -1
    for i in range(n):
        x = int(raw_input())
        w.append(x)
        maxv = max(maxv, x)

    left = 0
    right = n * maxv

    # range: (left, right]
    # loop until left + 1 = right, then right is the answer
    # why? because right works, but right - 1 doesn't work
    # so right is the smallest capacity
    while right - left > 1:
        mid = (left + right) / 2
        v = f(w, n, k, mid)
        if v >= n:
            # range: (left, mid]
            # in fact, v cannot > n
            right = mid
        else:
            # range: (mid, right]
            left = mid
    print right
