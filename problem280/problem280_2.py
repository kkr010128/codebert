n=int(input())
x=[]
y=[]
for i in range(n):
    a,b=map(int,input().split())
    x.append(a)
    y.append(b)

p=1
for i in range(n):
    p*=i+1

def D(a,b):
    a=a-1
    b=b-1
    return ((x[a]-x[b])**2+(y[a]-y[b])**2)**(0.5)

def f(x):
    ans=0
    while x>0:
        ans+=x%2
        x=x//2
    return ans

def r(x):
    ans=1
    for i in range(x):
        ans*=(i+1)
    return ans

dp=[[0]*(n+1) for _ in range(2**n)]
for i in range(1,2**n):
    for j in range(1,n+1):
        for k in range(1,n+1):
            if (i>>(j-1))&1 and not (i>>(k-1)&1):
                dp[i+2**(k-1)][k]+=dp[i][j]+r((f(i)-1))*D(j,k)

print(sum(dp[2**n-1])/p)

