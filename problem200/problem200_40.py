A,B,M=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
D=[]
for i in range(M):
    D.append(list(map(int,input().split())))
    
S=min(a)+min(b)
P=[]
for i in range(M):
    P.append(a[D[i][0]-1]+b[D[i][1]-1]-D[i][2])
P.append(S)
print(min(P))