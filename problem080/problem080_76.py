N=int(input())
Z=[0]*N
W=[0]*N

for i in range(N):
    x,y=map(int,input().split())
    Z[i]=x+y
    W[i]=x-y

alpha=max(Z)-min(Z)
beta=max(W)-min(W)
print(max(alpha,beta))