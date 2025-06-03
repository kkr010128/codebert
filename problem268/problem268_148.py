# https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_e

import sys
input=sys.stdin.readline
MOD=10**9+7

def main():
    N=int(input())
    A=list(map(int,input().split()))
    cnt=[0]*N
    ans=1
    for i in range(N):
        if A[i]==0:
            ans*=3-cnt[0]
            ans%=MOD
            cnt[A[i]]+=1
        else:
            ans*=cnt[A[i]-1]-cnt[A[i]]
            ans%=MOD
            cnt[A[i]]+=1
    print(ans)
        
    
    
    
if __name__=="__main__":
    main()
