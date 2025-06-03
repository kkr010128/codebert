def fib(n):
    a=[1,1]
    for i in range(2,n+1):
        a.append(a[i-2]+a[i-1])
        i+=1
    return a[-1]
    
n=int(input())
print(fib(n))
