def gcd(x,y):
    if x%y!=0:
        return gcd(y,x%y)
    else:
        return y
def GCD(x,y,z):
    return gcd(gcd(x,y),z)
ans=0
K=int(input())
for a in range(1,K+1):
    for b in range(1,K+1):
        for c in range(1,K+1):
            ans+=GCD(a,b,c)
print(ans)
