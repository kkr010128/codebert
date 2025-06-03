import sys
input = sys.stdin.buffer.readline
import copy

def main():
    N,K = map(int,input().split())
    MOD = 10**9+7

    fac = [0 for _ in range(2*10**5+1)]
    fac[0],fac[1] = 1,1
    inv = copy.deepcopy(fac)
    invfac = copy.deepcopy(fac)
    
    for i in range(2,2*10**5+1):
        fac[i] = (fac[i-1]*i)%MOD
        inv[i] = MOD-(MOD//i)*inv[MOD%i]%MOD
        invfac[i] = (invfac[i-1]*inv[i])%MOD

    def coef(x,y):
        num = (((fac[x]*invfac[y])%MOD)*invfac[x-y]%MOD)
        return num
    
    ans = 0
    for i in range(min(N,K+1)):
        a = coef(N,i)
        b = coef(N-1,N-i-1)
        ans += ((a*b)%MOD)
        
    print(ans%MOD)
    
if __name__ == "__main__":
    main()