import sys
input = sys.stdin.readline

def gcd(a,b):
    while b:
        a,b=b,a%b
    return a


def prime_factor(n):
    a=[]
    while n%2==0:
        a.append(2)
        n//=2
    f=3
    while f*f<=n:
        if n%f==0:
            a.append(f)
            n//=f
        else:
            f+=2
    if n!=1:
        a.append(n)
    return set(a)




n=int(input())
L=list(map(int,input().split()))
val = L[0]

for i in range(1,n):
    val = gcd(L[i],val)

if val!=1:
    print('not coprime')
    sys.exit()

d={}
for i in range(n):
    factor=prime_factor(L[i])
    for j in factor:
        if j not in d:
            d[j]=1
        else:
            print('setwise coprime')
            sys.exit()
print('pairwise coprime')


