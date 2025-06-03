s=int(input())
p=10**9+7
if s<=2:
    print(0)
    exit()
n=s//3
ans=0
x=[0]*(s+1)
x[0]=1
x[1]=1
y=[0]*(s+1)

for i in range(2,s+1):
    x[i]=x[i-1]*i%p

y[s]=pow(x[s],p-2,p)
for i in range(s):
    y[s-1-i]=y[s-i]*(s-i)%p

for k in range(1,n+1):
    ans+=x[s-2*k-1]*y[k-1]*y[s-3*k]%p

print(ans%p)

