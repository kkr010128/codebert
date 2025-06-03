#

import sys
input=sys.stdin.readline

def main():
    N,K=map(int,input().split())
    A=list(map(lambda x: int(x)-1,input().split()))
    latest=[-1]*N
    latest[0]=0
    now=0
    while(K>0):
        K-=1
        to=A[now]
        if latest[A[now]]!=-1:
            K%=latest[now]-latest[A[now]]+1
        latest[A[now]]=latest[now]+1
        now=to
    print(now+1)
        
if __name__=="__main__":
    main()
