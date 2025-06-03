import sys


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    h, w, k = list(map(int, readline().split()))
    s = [list(str(readline().rstrip().decode('utf-8'))) for _ in range(h)]
    cnt = 0
    ls = []
    lsd = -1
    for i in range(h):
        if s[i].count("#") != 0:
            lsd = i
            is_f = True
            cnt += 1
            for j in range(w):
                if s[i][j] == "#":
                    if is_f:
                        is_f = False
                    else:
                        cnt += 1
                s[i][j] = cnt
            while ls:
                ti = ls.pop()
                for j in range(w):
                    s[ti][j] = s[i][j]
        else:
            ls.append(i)
            if i == h - 1:
                while ls:
                    ti = ls.pop()
                    for j in range(w):
                        s[ti][j] = s[lsd][j]
    for i in range(len(s)):
        print(*s[i])


if __name__ == '__main__':
    solve()
