A,B,C,K=map(int,input().split())

ans=1*min(A,K)
K=max(0,K-A-B)
print(ans-(1*K))
