n,k=map(int,input().split())
L=[list(map(int, input().split())) for i in range(2*k)]
X=[]
for i in range(1,2*k,2):
  X.extend(L[i])
x=0
print(n-len(set(X)))