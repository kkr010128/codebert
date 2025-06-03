n, k = map(int, input().split())

mod = 10**9+7

def power(a, n, mod):
    bi=str(format(n,"b")) #2進数
    res=1
    for i in range(len(bi)):
        res=(res*res) %mod
        if bi[i]=="1":
            res=(res*a) %mod
    return res

X = [0]*(k+1)

ans = 0
for g in reversed(range(1, k+1)):
    temp = power(k//g, n, mod)
    j = g
    while j <= k:
        temp -= X[j]
        j += g
    ans += temp*g
    X[g] = temp
ans %= mod
print(ans)
