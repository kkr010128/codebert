import sys
sys.setrecursionlimit(2147483647)
INF = 1 << 60
MOD = 10**9 + 7 # 998244353
input = lambda:sys.stdin.readline().rstrip()
from functools import cmp_to_key
def resolve():
    n = int(input())
    first, second, third = [], [], []
    for _ in range(n):
        balance = min_balance = 0
        for c in input():
            if c == '(':
                balance += 1
            else:
                balance -= 1
            min_balance = min(min_balance, balance)
        if min_balance == 0:
            first.append((min_balance, balance))
        elif balance > 0:
            second.append((min_balance, balance))
        else:
            third.append((min_balance, balance))

    now = 0
    # first は何も考えず足せば良い
    for min_balance, balance in first:
        now += balance

    # second は min_balance の大きい方から足せば良い
    second.sort(reverse = 1)
    for min_balance, balance in second:
        if now + min_balance < 0:
            print("No")
            return
        now += balance

    # third は sort を工夫
    def cmp(s1, s2):
        m1, b1 = s1
        m2, b2 = s2
        return -1 if min(m1, b1 + m2) > min(m2, b2 + m1) else 1

    third.sort(key = cmp_to_key(cmp))
    for min_balance, balance in third:
        if now + min_balance < 0:
            print("No")
            return
        now += balance

    print("Yes" if now == 0 else "No")
resolve()