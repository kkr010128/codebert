l=input().split()
n=int(l[0])
m=int(l[1])

#receive vecter a(n*m)
i=0
A=[]
while i<n:
    a=input().split()
    for p in a:
        A.append(int(p))
    i+=1

#receive vecter b(m*1)
I=0
B=[]
while I<m:
    b=int(input())
    B.append(b)
    I+=1

#Ci=ai1b1+ai2b2+...+aimbm
#C[i]=a[m*(i)+1]*b[1]+a[m*(i)+2]*b[2]+...a[m*(i)+m]*b[m]
q=0
C=[]
while q<n:
    Q=0
    cq=0
    while Q<m:
        cq+=A[m*q+Q]*B[Q]
        Q+=1
    C.append(cq)
    q+=1

for x in C:
    print(x)
