X,Y=list(map(int, input().split()))
a=(2*X-Y)//3
b=(2*Y-X)//3
if not (2*a+b==X and a+2*b==Y and a>=0 and b>=0):
    print(0)
    exit()

C=10**9+7
A=1
B=1
D=1
for i in range(a):
    A*=i+1
    A=A%C
for j in range(b):
    B*=j+1
    B=B%C
for k in range(a+b):
    D*=k+1
    D=D%C

D*=pow(A,C-2,C)
D*=pow(B,C-2,C)
print(D%C)