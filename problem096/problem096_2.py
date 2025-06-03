N,D=map(int,input().split())
X=[]
for i in range(N):
    X.append(list(map(int,input().split())))
count=0
for i in range(N):
    if pow(X[i][0]*X[i][0]+X[i][1]*X[i][1],1/2)<=D:count+=1
print(count)