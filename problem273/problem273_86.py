import sys
sys.setrecursionlimit(10**9)
INF=10**18
def input():
    return sys.stdin.readline().rstrip()

def main():
    N,K=map(int,input().split())
    A=list(map(int,input().split()))
    B=[0]*(N+1)
    for i in range(N):
        B[i+1]=(A[i]+B[i]-1)%K
    ans=0
    d={}
    for i in range(1,N+1):
        if i-K<0:
            if B[i-1] in d:
                d[B[i-1]]+=1
            else:
                d[B[i-1]]=1
        else:
            if B[i-1] in d:
                d[B[i-1]]+=1
            else:
                d[B[i-1]]=1
            d[B[i-K]]-=1
        if B[i] in d:
            ans+=d[B[i]]
    print(ans)
    

if __name__ == '__main__':
    main()
