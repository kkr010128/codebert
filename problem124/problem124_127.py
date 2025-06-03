#atcoder template
def main():
    import sys
    imput = sys.stdin.readline
    #文字列入力の時は上記はerrorとなる。
    #ここにコード

    #N = 1のときなどcorner caseを確認！
if __name__ == "__main__":
    main()

#input
K = int(input())
S = str(input())

#output
# (o以外) o (o以外) o (f以外) f (何でも)

#こちらもmodで割った余り。maxが決まっていて、大きくない時はこちらが早い。
mod = pow(10, 9) + 7

n_ = 5 * pow(10, 6)
fun = [1] * (n_+1)
for i in range(1, n_+1):
    fun[i] = fun[i-1] * i % mod
rev = [1] * (n_+1)
rev[n_] = pow(fun[n_], mod-2, mod)
for i in range(n_-1, 0, -1):
    rev[i] = rev[i+1] * (i+1) % mod
def cmb(n,r):
    if n < 0 or r < 0 or r > n: return 0
    return fun[n] * rev[r] % mod * rev[n-r] % mod

#重複組み合わせはH(n, r) = cmb(n+r-1, r)

L = len(S)
answer = 0
for i in range(L, L+K+1):
    answer += pow(25, i-L, mod) * pow(26, L+K-i, mod) * cmb(i-1, L-1)
    answer %= mod
print(answer)