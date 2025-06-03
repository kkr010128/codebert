def fib(n):
    if n==0 or n==1:
        return 1
    else:
        if f[n]!=0:
            return f[n]
        else:
            f[n]=fib(n-1)+fib(n-2)
            return f[n]
f=[0]*45
n=int(input())

print(fib(n))
