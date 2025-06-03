import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from fractions import gcd

    n, m = list(map(int, readline().split()))
    a = list(map(int, readline().split()))
    cnt = [0] * n

    for i, elem in enumerate(a):
        x = elem
        c = 0
        while x % 2 == 0:
            x //= 2
            c += 1
        cnt[i] = c

    ans = 0

    if len(set(cnt)) == 1:
        lcm = a[0]
        for elem in a[1:]:
            lcm = (lcm * elem) // gcd(lcm, elem)
        ans = (m + (lcm // 2)) // lcm

    print(ans)


if __name__ == '__main__':
    main()
