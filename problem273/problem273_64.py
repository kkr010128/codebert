import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
from collections import defaultdict
def resolve():
    n,k=map(int,input().split())
    A=list(map(lambda x:int(x)-1,input().split()))
    S=[0]*(n+1)
    for i in range(n):
        S[i+1]=S[i]+A[i]
        S[i+1]%=k

    C=defaultdict(int)
    ans=0
    for i in range(n+1):
        ans+=C[S[i]]
        C[S[i]]+=1
        if(i-k+1>=0): C[S[i-k+1]]-=1
    print(ans)
resolve()