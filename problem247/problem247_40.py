from fractions import gcd
n, m = map(int, input().split())
a = list(map(int, input().split()))

def lcm(a, b):
    return a*b // gcd(a, b)
"""
akが偶数だから、bk=2akとして、
bk × (2p + 1)を満たすpが存在すれば良い
2p+1は奇数のため、Xとbkの2の素因数は一致しなければならない
akに含まれる最大の2^kを探す。
"""
if len(a) == 1: lcm_all = a[0]//2
else: lcm_all = lcm(a[0]//2, a[1]//2)
amax = 0
for i in range(1, n):
    lcm_all = lcm(lcm_all, a[i]//2)
    amax = max(amax, a[i]//2)

f = True
if lcm_all > m:
    f = False
for i in range(n):
    if n == 1: break
    if (lcm_all//(a[i]//2))%2 == 0:
        # akの2の約数の数がそろわないので、どんな奇数を掛けても共通のXを作れない
        f = False
if f:
    # amaxの奇数倍でmを超えないもの
    ans = (m // lcm_all + 1)//2
    print(ans)
else:
    print(0)