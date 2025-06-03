import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    M=65
    A=LI()
    cnt=[0]*M
    
    for i in range(N):
        a=A[i]
        for j in range(M):
            if a>>j & 1:
                cnt[j]+=1
                
    ans=0
    for i in range(M):
        a=cnt[i]
        b=N-a
        ans=(ans + a*b*pow(2,i,mod))%mod
        
    print(ans)
                

main()
