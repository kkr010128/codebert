import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())

    cnt = [[0] * 10 for _ in range(10)]
    for i in range(1, n + 1):
        i = str(i)
        head = int(i[0])
        foot = int(i[-1])
        cnt[head][foot] += 1

    res = 0
    for i in range(1, n + 1):
        i = str(i)
        head = int(i[0])
        foot = int(i[-1])
        res += cnt[foot][head]
    print(res)


if __name__ == '__main__':
    resolve()
