sum=0
s=0
A=input().split()
n=(int)(A[0])
t=(int)(A[1])
x=[0 for i in range(2*n)]
for i in range(n):
    B=input().split()
    k=2*i
    x[k]=(B[0])
    x[k+1]=(int)(B[1])
while len(x)>0:
    s=x[1]-t
    if s>0: 
        sum+=t
        x.append(x[0])
        x.append(s)
        del x[0]
        del x[0]
    if s<=0:
        sum+=x[1]
        print( x[0],sum)
        del x[0]
        del x[0]

