r=input().split()
N=int(r[0])
A=int(r[1])
B=int(r[2])
x=N//(A+B)
y=N%(A+B)
if y<=A:
    print(A*x+y)
else:
    print(A*(x+1))