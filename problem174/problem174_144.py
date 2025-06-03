k=int(input())

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

ans=0
for i in range(1,k+1):
    for j in range(1,k+1):
        for l in range(1,k+1):
            ans+=gcd(gcd(i,j),l)
print(ans)