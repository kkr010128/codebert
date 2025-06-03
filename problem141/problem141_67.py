# coding: utf-8


def solve(*args: str) -> str:
    n = int(args[0])
    A = list(map(int, args[1].split()))

    if 0 < A[0]:
        return '1' if n == 0 and A[0] == 1 else '-1'

    R = [0]*(n+1)
    R[0] = 1
    for i in range(1, n+1):
        R[i] = 2*(R[i-1]-A[i-1])

    prev = 0
    ret = 0
    for i in range(n, -1, -1):
        if R[i] < A[i]:
            ret = -1
            break

        prev = min(R[i], A[i]+prev)
        ret += prev

    return str(ret)


if __name__ == "__main__":
    print(solve(*(open(0).read().splitlines())))
