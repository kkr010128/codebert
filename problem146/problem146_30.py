import sys
from collections import defaultdict
from math import gcd
def input(): return sys.stdin.readline().strip()
mod = 1000000007

def main():
    N = int(input())
    fish = defaultdict(int)

    """
    b / aで値を管理するのは浮動小数点誤差が怖いので、
    g = gcd(a, b) として(a//g, b//g)のタプルで管理するのが良い。
    """

    zero = 0
    for _ in range(N):
        a, b = map(int, input().split())
        if a == 0 and b == 0: zero += 1
        elif a == 0: fish[(0, 1)] += 1
        elif b == 0: fish[(1, 0)] += 1
        else:
            g = gcd(a, b)
            if a < 0: a, b = -a, -b
            fish[(a // g, b // g)] += 1
    #print(fish)
    
    """
    仲の悪い組を(S1, T1), (S2, T2),...とすれば(Si, Ti)からの魚の選び方と
    (Sj, Tj)からの魚の選び方は独立じゃん。
    なぜ気づかなかったのか。。。
    """
    
    ans = 1
    finished = set([])
    for a, b in fish:
        if (a, b) in finished: continue
        finished.add((a, b))
        s = fish[(a, b)]
        if b > 0:
            t = fish[(b, -a)] if (b, -a) in fish else 0
            finished.add((b, -a))
        else:
            t = fish[(-b, a)] if (-b, a) in fish else 0
            finished.add((-b, a))
        ans *= pow(2, s, mod) + pow(2, t, mod) - 1
        ans %= mod
        #print("(a, b)=({}, {}) -> s={}, t={}, val={}".format(a, b, s, t, pow(2, s, mod) + pow(2, t, mod) - 1))
    print((ans + zero - 1) % mod)



if __name__ == "__main__":
    main()
