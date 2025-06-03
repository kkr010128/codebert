n = int(input())
MOD = 10**9+7
a=10
b=9
c=8
for i in range(n-1):
    a*=10
    b*=9
    c*=8
    if i%10==0:
        a=a%MOD
        b=b%MOD
        c=c%MOD

a=a%MOD
b=b%MOD
c=c%MOD
ans = (a-2*b+c)%MOD
print(ans)