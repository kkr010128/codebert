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

    T1, T2 = in_nn()
    A1, A2 = in_nn()
    B1, B2 = in_nn()

    if A1 > B1:
        A1, B1 = B1, A1
        A2, B2 = B2, A2

    da1 = T1 * A1
    da2 = T2 * A2
    db1 = T1 * B1
    db2 = T2 * B2

    if da1 == db1:
        if db1 == db2:
            ans = "infinity"
        else:
            ans = 1
    else:
        if da1 + da2 == db1 + db2:
            ans = "infinity"
        elif da1 + da2 < db1 + db2:
            ans = 0
        else:
            d1 = db1 - da1
            d2 = (da1 + da2) - (db1 + db2)
            ans = 1 + (d1 // d2) * 2
            if d1 % d2 == 0:
                ans -= 1

    print(ans)


if __name__ == '__main__':
    main()
