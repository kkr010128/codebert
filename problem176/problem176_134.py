# E - Sum of gcd of Tuples (Hard)

n, k = map(int, input().split())
X = [0]*(k+1)
mod = 10**9+7

for x in range(k, 0, -1):
    #X[x] = ((k//x)**n)%mod
    X[x] = pow(k//x, n, mod)
    for x_multi in range(x*2, k+1, x):
        X[x] -= X[x_multi]

print(sum((i*x)for i, x in enumerate(X))%mod)