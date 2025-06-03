def fib(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        a,b=1,2
        for i in range(n-2):
            a,b=b,a+b
        return b    

print(fib(int(input())))

