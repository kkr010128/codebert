N,K = map(int,input().split())
res = [0]*(K+1)
ans = 0
MOD = 10**9+7
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors

for k in range(K,0,-1):
    y = make_divisors(k)
    s = K//k
    tmp = pow(s, N, MOD)
    val = tmp-res[k]
    ans += k*val
    for yy in y:
        res[yy] += val
print(ans%MOD)
