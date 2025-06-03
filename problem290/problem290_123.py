def is_good(mid, key):
    ret = 0
    for i in range(N):
        ret += max(0, A[i] - mid // F[i])
    return ret <= key


def binary_search(key):
    bad, good = -1, 10 ** 18
    while good - bad > 1:
        mid = (bad + good) // 2
        if is_good(mid, key):
            good = mid
        else:
            bad = mid
    return good


N, K = map(int, input().split())
A = sorted(map(int, input().split()))
F = sorted(map(int, input().split()), reverse=True)
print(binary_search(K))
