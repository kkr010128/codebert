N,K=map(int,input().split())
P=list(map(int,input().split()))
P.sort()
b=0

for i in range(K):
    b+=P[i]
    
print(b)