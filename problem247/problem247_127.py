from fractions import gcd
from functools import reduce

def lcm(a,b): # lcmは標準ライブラリには存在しない
    return a * b // gcd(a,b)
def ls_lcm(A): # リストを引数に取れる
    return reduce(lcm ,A)
def ls_gcd(A): # リストを引数に取れる
    return reduce (gcd, A)

def count_two(n): # 2で割れる回数を取得
    cnt = 0
    while(n & 1 == 0): # 最下位ビットが0かどうか
        cnt += 1
        n = n >> 1 # 右ビットシフト
    return cnt

N, M = map(int, input().split())
A = list(map(int, input().split()))

if len(set([count_two(a) for a in A])) != 1:
    print (0)
    exit()
A = [a//2 for a in A] # a_k/2 を考える
lc = ls_lcm(A)
print ((M + lc) // (2*lc)) # 最小公倍数を奇数倍したものが条件を満たす
