def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

mod=1000000007
n=input();
arr = list(map(int, raw_input().split()))
l=arr[0];
for i in arr:
    x=gcd(l,i)
    l=(l*i)/x
    
ans=0
#print l
for i in arr:
    b=l/i
    ans+=b
ans=(ans%mod +mod)%mod
print ans
