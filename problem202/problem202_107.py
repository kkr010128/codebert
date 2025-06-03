N,A,B = map(int,input().split())
a = N//(A+B)
b = N%(A+B)
if b>A:
    print(a*A+A)
else:
    print(a*A+b)