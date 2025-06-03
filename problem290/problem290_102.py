def check(T, K, A, F):
    # check whether all members finish by the time T
    counts = [max(0, (a * f - T + f - 1) // f) for a, f in zip(A, F)]  # math.ceil((a * f - T) / f)
    return sum(counts) <= K


def main():
    N, K = list(map(int, input().split(' ')))
    A = list(map(int, input().split(' ')))
    A.sort()
    F = list(map(int, input().split(' ')))
    F.sort(reverse=True)
    ok = 10 ** 12
    ng = - 1
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if check(mid, K, A, F):
            ok = mid
        else:
            ng = mid
    print(ok)


if __name__ == '__main__':
    main()
