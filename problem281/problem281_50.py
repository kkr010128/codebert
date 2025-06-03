import sys

p=10**9+7

x,y=map(int,input().split())

if (x+y)%3!=0 or x>2*y or y>2*x:
    print(0)
    sys.exit()

a=(-x+2*y)//3
b=(2*x-y)//3

A=1
for i in range(1,a+1):
    A=A*i
    A=A%p
B=1
for i in range(1,b+1):
    B=B*i
    B=B%p

AB=1
for i in range(1,a+b+1):
    AB=AB*i
    AB=AB%p

C=(AB*pow(A,p-2,p)*pow(B,p-2,p))%p

print(C)