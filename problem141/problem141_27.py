import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
    N = int(input())
    A = list(map(int, input().split()))

    if A[0] != 0:
        if N == 0 and A[0] == 1:
            print('1')
            exit()
        else:
            print('-1')
            exit()

    if N == 0:
        print('1')
        exit()

    v = [0 for _ in range(N + 1)]
    v[N] = A[N]

    for i in range(N - 1, -1, -1):
        up = min(2 ** i, v[i + 1] + A[i])
        v[i] = up

    # print(v)
    for i in range(N):
        up = min(v[i + 1], (v[i] - A[i]) * 2)
        v[i + 1] = up

    # print(v)
    ans = 0
    for i in range(N + 1):
        if v[i] < A[i]:
            print('-1')
            exit()
        ans += v[i]

    # print(v)
    print(ans)


if __name__ == '__main__':
    solve()
