def fib(n):
    x=[1,1]
    for i in range(n+1):
        y=x[i]+x[i+1]
        x.append(y)
    print(x[n])
    
a=int(input())
fib(a)
