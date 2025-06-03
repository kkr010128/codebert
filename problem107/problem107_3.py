import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    X = input()

    cnt_init = X.count("1")
    x_init = int(X, 2)
    a = x_init % (cnt_init + 1)
    if cnt_init - 1 != 0:
        b = x_init % (cnt_init - 1)

    for i in range(n):
        if X[i] == "0":
            cnt = cnt_init + 1
            x = (a + pow(2, (n - i - 1), cnt)) % cnt
            res = 1
        else:
            cnt = cnt_init - 1
            if cnt != 0:
                x = (b - pow(2, (n - i - 1), cnt)) % cnt
                res = 1
            else:
                x = 0
                res = 0

        while x:
            cnt = bin(x).count("1")
            x %= cnt
            res += 1
        print(res)


if __name__ == '__main__':
    resolve()
