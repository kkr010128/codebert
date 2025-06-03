K=int(input())
def gcd(p,q):
    if p%q==0:
        return q
    return gcd(q,p%q)
S=0
for i in range(K):
    for j in range(K):
        for k in range(K):
            S+=gcd(i+1,gcd(j+1,k+1))
print(S)