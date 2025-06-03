from math import floor

A,B,N=map(int,input().split())

ans=A*(B-1)//B

if N<B:
    ans=A*N//B
print(ans)