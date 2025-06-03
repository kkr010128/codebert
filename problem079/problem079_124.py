def main():
    mod=1000000007
    s=int(input())
    
    m=s*2
    inv=lambda x: pow(x,mod-2,mod)
    Fact=[1] #階乗
    for i in range(1,m+1):
        Fact.append(Fact[i-1]*i%mod)
    Finv=[0]*(m+1) #階乗の逆元
    Finv[-1]=inv(Fact[-1])
    for i in range(m-1,-1,-1):
        Finv[i]=Finv[i+1]*(i+1)%mod
    def comb(n,r):
        if n<r:
            return 0
        return Fact[n]*Finv[r]*Finv[n-r]%mod
    
    ans=0
    num=s//3
    for i in range(1,num+1):
        n=s-i*3
        ans+=comb(n+i-1,n)
        ans%=mod
    print(ans)
    
if __name__=='__main__':
    main()