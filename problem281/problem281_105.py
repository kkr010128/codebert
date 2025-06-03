N=10**9+7
x , y = map(int, input().split())
a=(2*x-y)//3
b=(2*y-x)//3

if 2*a+b!=x:
    print(0)
    exit()

n=a+b
r=a

def fac(n,r,N):
    ans=1
    for i in range(r):
        ans=ans*(n-i)%N
    return ans

def combi(n,r,N):
    if n<r or n<0 or r<0:
        ans = 0
        return ans
    r= min(r, n-r)
    ans = fac(n,r,N)*pow(fac(r,r,N),N-2,N)%N
    return ans

ans = combi(n,r,N)
print(ans)
