from bisect import bisect_left


def calc(N, A, cumsum, x):
    num = N ** 2
    total = cumsum[N] * N * 2
    for a in A:
        idx = bisect_left(A, x - a)
        num -= idx
        total -= cumsum[idx] + idx * a
    return num, total


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    cumsum = [0] * (N+1)
    for i in range(N):
        cumsum[i+1] = cumsum[i] + A[i]
    lo = 0
    hi = int(2e5+1)
    while lo < hi:
        mid = (lo + hi) // 2
        num, total = calc(N, A, cumsum, mid)
        if num <= M:
            hi = mid
        else:
            lo = mid + 1
    num, total = calc(N, A, cumsum, lo)
    ans = total - (num - M) * (lo - 1)
    print(ans)


if __name__ == "__main__":
    main()
