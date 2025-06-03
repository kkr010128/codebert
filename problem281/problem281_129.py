# ABC145D

import sys
input=sys.stdin.readline
MOD=10**9+7

factorial=[1]*(2*10**6+1)
for i in range(1,2*10**6+1):
    factorial[i]=factorial[i-1]*i
    factorial[i]%=MOD

def modinv(x):
    return pow(x,MOD-2,MOD)
    
def comb(n,r):
    return (factorial[n]*modinv(factorial[n-r])*modinv(factorial[r]))%MOD

def main():
    X,Y=map(int,input().split())
    a=(2*Y-X)
    b=(2*X-Y)
    A=a//3
    B=b//3
    ans=0
    if a%3==0 and b%3==0 and a>=0 and b>=0:
        ans=comb(A+B,A)
    print(ans)
    
    
    
if __name__=="__main__":
    main()
