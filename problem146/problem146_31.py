import math
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

def main():
    n = int(input())
    mod = 10 ** 9 + 7
    h = {}
    zero = 0
    for i in range(n):
        a, b = map(int, input().split())
        if a == 0 and b == 0:
            zero += 1
            continue
        m = (0, 0)
        if b == 0:
            m = (1, 0)
        elif b > 0:
            g = math.gcd(a, b)
            m = (a // g, b // g)
        else:
            g = math.gcd(a, b)
            m = (-1 * (a // g), -1 * (b // g))
        if m not in h:
            h[m] = set()
        h[m].add(i)
    h2 = {}
    for m in h:
        mi1 = (-1 * m[1], m[0])
        if mi1 in h and mi1 not in h2:
            h2[m] = mi1
        mi2 = (m[1], -1 * m[0])
        if mi2 in h and mi2 not in h2:
            h2[m] = mi2
    ans = 1
    left = n - zero
    for k, v in h2.items():
        s1 = len(h[k])
        s2 = len(h[v])
        # print(s1, s2)
        r = (pow(2, s1 + s2, mod) - (pow(2, s1, mod) - 1) * (pow(2, s2, mod) - 1)) % mod
        ans *= r
        ans %= mod
        left -= (s1 + s2)
    ans *= pow(2, left, mod)
    ans -= 1
    ans += zero
    print(ans % mod)

if __name__ == '__main__':
    main()
