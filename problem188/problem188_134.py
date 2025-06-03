q=list(map(int,input().split()))
X=q[0]
Y=q[1]
A=q[2]
B=q[3]
C=q[4]
r=list(map(int,input().split()))
g=list(map(int,input().split()))
n=list(map(int,input().split()))
r=sorted(r,reverse=True)
g=sorted(g,reverse=True)
n=sorted(n,reverse=True)
A=[]
for i in range(X):
    A.append(r[i])
for i in range(Y):
    A.append(g[i])
A=sorted(A,reverse=True)
s=0
for i in range(min(len(A),len(n))):
    if A[-1]>=n[i]:
        s=i
        break
    A.pop(-1)
    s=i+1
for i in range(s):
    A.append(n[i])
print(sum(A))




