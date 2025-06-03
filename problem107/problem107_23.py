import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    def solve(p):
        cur = p
        cnt = 1
        while cur > 0:
            pop = f'{cur:b}'.count("1")
            cur = cur % pop
            cnt += 1

        return cnt

    n = int(readline())
    s = input()

    c = s.count("1")
    cp = c + 1
    cm = c - 1

    fp = 0
    fm = 0

    for i, x in enumerate(s[::-1]):
        if x == "1":
            if cp <= n:
                fp += pow(2, i, cp)
                fp %= cp
            if cm > 0:
                fm += pow(2, i, cm)
                fm %= cm

    for i in range(n):
        if s[i] == "0":
            a = pow(2, n - (i + 1), cp)
            cur = (fp + a) % cp
            print(solve(cur))
        else:
            if cm > 0:
                a = pow(2, n - (i + 1), cm)
                cur = (fm - a) % cm
                print(solve(cur))
            else:
                print(0)


if __name__ == '__main__':
    main()
