import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
def main():
    n, *a = map(int, read().split())
    a.sort()
    a = tuple(a)
    TorF = [0] * (a[-1] + 1)
    for ae in a:
        TorF[ae] = 1
    for i1 in range(n - 1):
        a1 = a[i1]
        if TorF[a1]:
            m = a[-1] // a1 + 1
            for i2 in range(2, m):
                TorF[a1 * i2] = 0
        if a[i1 + 1] == a[i1]:
            TorF[a[i1]] = 0
    r = sum(TorF)
    print(r)

if __name__ == '__main__':
    main()