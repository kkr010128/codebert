import sys
input = sys.stdin.buffer.readline
import copy

def main():
    N,M = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    
    MOD = 10**9+7
    fac = [0 for _ in range(N+1)]
    fac[0],fac[1] = 1,1
    invfac = copy.deepcopy(fac)
    for i in range(2,N+1):
        fac[i] = (fac[i-1]*i)%MOD
        
    invfac[-1] = pow(fac[-1],MOD-2,MOD)
    for i in range(N,0,-1):
        invfac[i-1] = (invfac[i]*i)%MOD
    
    def coef(x,y):
        num = (((fac[x]*invfac[y])%MOD)*invfac[x-y]%MOD)
        return num
        
    p,m = 0,0
    for i in range(N-M+1):
        comb = coef(N-i-1,M-1)
        p += a[-i-1]*comb
        m += a[i]*comb

    print((p-m)%MOD)
    
if __name__ == "__main__":
    main()
