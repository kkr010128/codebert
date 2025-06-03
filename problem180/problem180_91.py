N,K=map(int,input().split())
x=N%K
y=abs(x-K)    
print(min(x,y))