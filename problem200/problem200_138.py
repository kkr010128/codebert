A,B,M=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
d=[]
for i in range(M):
    c.append(list(map(int,input().split())))
C=min(a)+min(b)
for i in range(0,M):
    d.append(a[(c[i][0]-1)]+b[(c[i][1]-1)]-c[i][2])
D=min(d)
print(min(C,D))