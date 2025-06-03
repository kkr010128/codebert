#事前に階乗を計算しておく maximにnの最大値をいれる
maxim = 10**6+1

MOD = 10**9+7
kaijou = [1]*(maxim)
for i in range(1,maxim):
    kaijou[i]=(kaijou[i-1]*i)%MOD
#nCr
def nCr(n,r):
    if n < r:
        return 0
    return ((kaijou[n]*pow(kaijou[r],MOD-2,MOD))%MOD*pow(kaijou[n-r],MOD-2,MOD))%MOD

#nHr
def nHr(n,r):
    if r == 0:
        if n == 0:
            return 1
        return 0
    return ((kaijou[n+r-1]*pow(kaijou[n],MOD-2,MOD))%MOD*pow(kaijou[r-1],MOD-2,MOD))%MOD

N = int(input())
ans = 0
for i in range(1,(N//3)+1):
    tmp = nHr(N-3*i,i)
    ans = (ans+tmp)%MOD

print(ans)