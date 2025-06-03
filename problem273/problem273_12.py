import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
from collections import defaultdict
def resolve():
    n,k=map(int,input().split())
    A=list(map(int,input().split()))
    S=[0]*(n+1)
    for i in range(n):
        S[i+1]=S[i]+A[i]
    for i in range(n+1):
        S[i]-=i
        S[i]%=k

    ans=0
    D=defaultdict(int)
    for i in range(n+1):
        s=S[i]
        ans+=D[s]
        D[s]+=1
        if(i>=k-1):
            D[S[i-k+1]]-=1
    print(ans)
resolve()