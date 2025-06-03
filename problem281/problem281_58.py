x,y = map(int,input().split())
mod = 10**9+7
def comb(N,x):
    numerator = 1
    for i in range(N-x+1,N+1):
        numerator = numerator * i % mod
    denominator = 1
    for j in range(1,x+1):
        denominator = denominator * j % mod
    d = pow(denominator,mod-2,mod)
    return numerator * d % mod

if (x+y) % 3 == 0:
    a = (2*y-x) //3
    b = (2*x-y) //3

    if a >= 0 and b >= 0:
        print(comb(a+b,a))
        exit()
print(0)