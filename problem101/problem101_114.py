# 3
A,B,C=map(int,input().split())
K=int(input())

def f(a,b,c,k):
    if k==0:
        return a<b<c
    return f(a*2,b,c,k-1) or f(a,b*2,c,k-1) or f(a,b,c*2,k-1)

print('Yes' if f(A,B,C,K) else 'No')

