X,Y,Z=map(int,input().split(" "))
tmp=Y
Y=X
X=tmp
tmp=Z
Z=X
X=tmp
print(X,Y,Z,end=" ")