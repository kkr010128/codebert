import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_nl = lambda: list(map(int, readline().split()))
in_na = lambda: map(int, read().split())
in_s = lambda: readline().rstrip().decode('utf-8')

INF = 10**9 + 7


def main():
    N = in_n()
    arms = [tuple()] * N

    for i in range(N):
        x, l = in_nn()
        arms[i] = (x - l, x + l)

    arms.sort(key=lambda x: x[1])
    # print(arms)

    r_max = -INF
    count = 0
    for i in range(N):
        l, r = arms[i]
        if r_max <= l:
            r_max = r
            count += 1

    print(count)


if __name__ == '__main__':
    main()
