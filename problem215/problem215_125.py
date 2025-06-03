n,k = map(int,input().split())

# Function of Combination mod M
# set n >= max p expected
M = 10**9+7


if k >= n-1:
    fac = [1]+[0]*(2*n-1)
    for i in range(1,2*n): fac[i] = fac[i-1]*i %M
    comb = lambda p,q:(fac[p]*pow(fac[q],M-2,M)*pow(fac[p-q],M-2,M))%M
    y = comb(2*n-1,n-1)
    
else:
    y = 1
    c1,c2=1,1
    for i in range(1,k+1):
        p = pow(i,M-2,M)
        c1 = c1*(n+1-i)*p%M
        c2 = c2*(n-i)*p%M
        y += c1*c2%M
        # y = (y+c1*c2)%M
print(y%M)
