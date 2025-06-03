n=int(input())
a=[1,1]
def fib(n):
    if n <= 1:
        return a[n]
    for i in range(2,n+1):
        a.append(a[i-1]+a[i-2])
    return a[n]
print(fib(n))
