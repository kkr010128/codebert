import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N = int(readline())

    def enum_divisors(n):
        # 約数列挙

        divisors = []

        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)

        return divisors

    divs = enum_divisors(N)

    ans = INF
    for div1 in divs:
        div2 = N // div1
        score = (div1 + div2 - 2)
        ans = min(score, ans)

    print(ans)


if __name__ == '__main__':
    main()
