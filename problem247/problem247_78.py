from fractions import gcd
def lcm(a,b):
    return a*b//gcd(a,b)
n,m=map(int,input().split())
a=list(map(int,input().split()))
h=list(map(lambda x:x//2,a))
l=1
for i in range(n):
    l=lcm(l,h[i])
for i in range(n):
    if (l//h[i])%2==0:
        print(0)
        exit()
print((m//l+1)//2)