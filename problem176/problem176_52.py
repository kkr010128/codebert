#ABC162-E Sum of gcd of Tuples(Hard)
"""
問題を「1~kまでの数字を用いた長さnの数列において、gcdがDになる数列はいくつあるか」
というふうに置き換える。(1<=D<=k)
更に制約を替えて、gcdが"Dの倍数"(但し,k以下)でも良いのでそれを全て求めよ、
というふうになった場合、全ての要素はD*n(nは整数,D*n<=k)となる。
この制約によって、そのような数列の数は(k/D)^nとして表せる。(これが大事)
例：
n = 3,k = 4の場合で、D(gcd)=2について求める
(4//2)**3 = 8※

そこで、大きい方からgcdがDになる数列の個数(これをメモ化)を求めていった場合、
Dの倍数がk以下であるならば、予めメモしておいたその値分を引いてやる。
これによって全ての通り数が求まる。
例の続き:
D=2について、D*n <= k という制約のもとでn=2が存在する。
D = 2*2 = 4の時の通り数は、4,4,4の1通り※なので、
D(gcd)=2となるパターン数は、※より、
8-1=7 となる。
(この7通りは2と4からなる数列で、全ての値が4になる場合を引いている)
"""
import sys
readline = sys.stdin.buffer.readline
n,k = map(int,readline().split())
mod = 10**9+7

ans = 0
count = [0]*(k+1)
for D in range(k,0,-1):
    mul = k//D #何倍まであり得るか(あり得るものをcountから引く)
    res = pow(mul,n,mod)
    for i in range(2,mul+1):
        res -= count[i*D]
    count[D] = res #個数
    ans += res*D #個数*値(求めたいのはgcdの合計値のため)
    ans %= mod

print(ans)