n=int(input())
def gcd(a,b):
    if b==0: return a
    else:
        return gcd(b,a%b)
def lcm(a,b):
    return a*b//gcd(a,b)


ans=0
for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            ans+= gcd(i,gcd(j,k))
print(ans)