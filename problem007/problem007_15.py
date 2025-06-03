def fib(n):
    a = 1
    b = 1
    if n == 0:
        print(a)
    elif n == 1:
        print(b)
    else:
        for i in range(n-1):
            c = a + b
            a , b = b , c
        print(c)

n = int(input())
fib(n)
