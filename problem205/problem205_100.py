# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10**9)
INF=10**18
MOD=2019
input=lambda: sys.stdin.readline().rstrip()
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

def main():
    N,P=map(int,input().split())
    A=list(map(int,list(input())[::-1]))
    ans=0
    if P==2 or P==5:
        if P==2:
            s=set([i*2 for i in range(5)])
        else:
            s=set([i*5 for i in range(2)])
        for i,x in enumerate(A[::-1],1):
            if x in s:
                ans+=i
    else:
        S=[0]*(N+1)
        for i in range(N):
            S[i+1]=(S[i]+A[i]*pow(10,i,P))%P
        l=[0]*P
        for i in range(N+1):
            ans+=l[S[i]]
            l[S[i]]+=1
    print(ans)


if __name__ == '__main__':
    main()

