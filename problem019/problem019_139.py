n,q = map(int,input().split())
A = []
B = []
C = []
t = 0

for i in range(n):
    x,y = input().split()
    A.append([x,int(y)])

while len(A)>0:
    f = A[0][1]
    if f<=q:
        t += f
        B.append(A[0][0])
        C.append(t)
    else:
        t += q
        A[0][1] -= q
        A.append(A[0])
    A.pop(0)

for j in range(len(B)):
    print(B[j],C[j])
