import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_s = lambda: readline().rstrip().decode('utf-8')
in_nl = lambda: list(map(int, readline().split()))
in_nl2 = lambda H: [in_nl() for _ in range(H)]
in_map = lambda: [s == ord('.') for s in readline() if s != ord('\n')]
in_map2 = lambda H: [in_map() for _ in range(H)]
in_all = lambda: map(int, read().split())


def main():
    a, b, c = in_nn()

    t1 = c - (a + b)
    t2 = 4 * a * b

    if t1 <= 0:
        print('No')
        exit()
    else:
        t1 = t1**2
        if t2 < t1:
            print('Yes')
        else:
            print('No')


if __name__ == '__main__':
    main()
