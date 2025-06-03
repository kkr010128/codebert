import sys


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    h, w, k = list(map(int, readline().split()))
    a = [list(str(readline().rstrip().decode('utf-8'))) for _ in range(h)]
    no = 0
    is_f = True
    for i in range(h):
        if a[i].count("#") != 0:
            row_f = True
            no += 1
            for j in range(w):
                if a[i][j] == "#":
                    if not row_f:
                        no += 1
                    else:
                        row_f = False
                a[i][j] = no
            if is_f:
                is_f = False
                if i != 0:
                    for j in range(i - 1, -1, -1):
                        for k in range(w):
                            a[j][k] = a[i][k]
        else:
            for j in range(w):
                a[i][j] = a[i-1][j]
    for i in range(h):
        print(*a[i])


if __name__ == '__main__':
    solve()
