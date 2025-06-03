#!/usr/bin/env python3

def pow(N,R,mod):
    ans = 1
    i = 0
    while((R>>i)>0):
        if (R>>i)&1:
            ans *= N
            ans %= mod
        N = (N*N)%mod
        i += 1
    return ans%mod


def main():
    N,K = map(int,input().split())
    li = [0 for _ in range(K)]

    mod = 10**9+7
    ans = 0
    for i in range(K,0,-1):
        mm = K//i
        mm = pow(mm,N,mod)

        for j in range(2,(K//i)+1):
            mm -= li[i*j-1]    
        li[i-1] = mm


        ans += (i*mm)%mod
        ans %= mod

    print(ans)

if __name__ == '__main__':
    main()

    

