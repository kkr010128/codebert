import copy

def com(n,r,m):
    #a = math.factorial(n)%m
    a = 1
    for i in range(1,n+1):
        a *= i
        a %= m
    A = pow(a,m-2,m)
    
    
    b= copy.copy(A)   
    for i in range(n,r,-1):
        b = (b*i)%m
    
    c = copy.copy(A)
    for i in range(n,n-r,-1):
        c = (c*i)%m
       
    return (a*b*c)%m

def main():
    k = int(input())
    s = input()
    mod = 10**9+7
    z = [1]
    for i in range(1,k+1):
        y = z[-1]*26
        z.append(y%mod)
    l = len(s)

    N = k+2
    inv_t = [0]+[1]
    for i in range(2,N):
        inv_t.append(inv_t[mod % i] * (mod - int(mod / i)) % mod)
    #print(inv_t)
    
    ans = 0
    p = 1   #pow(25,i-len(s),mod)
    #q = z[k]
    bai = 1
    for i in range(l,l+k+1):
        #base = p*q   #pow(26,len(s)+k-i,mod)
        #base = pow(25,i-len(s),mod) * pow(26,len(s)+k-i,mod)
        #bai = r
        #bai = com(i-1,len(s)-1,mod)
        #print(i,len(s),base,bai)
        ans += p*z[l+k-i]*bai
        ans %= mod
        p *= 25
        p %= mod
        #q = z[l+k-i-1]
        bai = bai*i*inv_t[i+1-l]
        bai %= mod
    print(ans)
    
if __name__=="__main__":
    main()