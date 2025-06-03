import sys, bisect, math, itertools, heapq, collections
from operator import itemgetter
# a.sort(key=itemgetter(i)) # i番目要素でsort
from functools import lru_cache
# @lru_cache(maxsize=None)
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp():
    '''
    一つの整数
    '''
    return int(input())
def inpl():
    '''
    一行に複数の整数
    '''
    return list(map(int, input().split()))

n, k = inpl()
ans = [0] * (k+1)
for i in range(k, 0, -1):
    ans[i] = pow(k // i, n, mod)
    for j in range(2, k+1):
        if i * j > k:
            break
        ans[i] -= ans[i * j]

# print(ans)
print(sum([ans[i]*i%mod for i in range(1,k+1)])%mod)

'''
1以上K以下の整数からなる長さNの数列{A_1,...A_N}を考える。
K^N個考えられる数列のgcd(A_1,...A_N)の和を求め、10^9+7で割った余りを出力せよ。

term:
2<=N<=10**5
1<=K<=10**5
input:
3 2
output:
    9
'''

'''
K^N個の数列すべてに対してgcdを計算しているとO((K^N)*(N+logK))になり間に合わない。
そこで、問題を
「1<=X<=Kに対してgcd(A_1,...A_N)=Xとなる数列A_iがいくつあるか」
という問題に読み替える。
Xが最大公約数であるためには{A_1,...A_N}がすべてXの倍数でなければならない。
K以下でXの倍数である数の個数はK//Xで求められる。
これらによって構成される数列は(K//X)^N種類ある。
しかしgcdがXの倍数であるものも含まれてしまうのでそれを包除原理で除く。
ex)
    K=4,N=3のとき(4,4,4)はすべて2の倍数だがgcdは4。
    したがって{(4//2)^3-(4//(2*2))^3}%modとする。
'''