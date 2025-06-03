import sys

read = sys.stdin.buffer.read


def main():
    N, K, *AF = map(int, read().split())
    A = AF[:N]
    F = AF[N:]

    A.sort()
    F.sort(reverse=True)

    ok = pow(10, 12)
    ng = -1
    while ok - ng > 1:
        mid = (ok + ng) // 2

        k = 0
        for i in range(N):
            if A[i] * F[i] > mid:
                k += A[i] - mid // F[i]

        if k <= K:
            ok = mid
        else:
            ng = mid

    print(ok)
    return


if __name__ == '__main__':
    main()
