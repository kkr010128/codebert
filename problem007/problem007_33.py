n = int(input())
a = int(0)
b = int(1)

if n==1:
    A = b
elif n==2:
    A = 2
else:
    for i in range(n):
        a,b = b,a+b
        A = b

print(A)
