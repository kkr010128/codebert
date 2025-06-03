H1,M1,H2,M2,K=map(int,input().split())

t1=60*H1 + M1
t2=60*H2 + M2
t=t2 - K
ans=t-t1
print(max(0,ans))