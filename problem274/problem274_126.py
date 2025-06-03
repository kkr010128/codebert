import sys


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    n, m = list(map(int, readline().split()))
    s = str(readline().rstrip().decode('utf-8'))
    res = []
    start = n
    while True:
        b = False
        for j in range(max(0, start - m), start):
            if s[j] == "0":
                res.append(start - j)
                start = j
                b = True
                break
        if not b:
            print(-1)
            exit()
        else:
            if j == 0:
                res.reverse()
                print(*res)
                exit()


if __name__ == '__main__':
    solve()
