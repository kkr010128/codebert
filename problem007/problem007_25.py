n = int(input())
def fib(n):
    m = [1,1]
    if n==0 or n==1:
        m=[1]
    else:
        for k in range(2,n+1):
            m.append(m[-1]+m[-2])
    return m

if n==0:
    l = fib(n)[n]
elif n==1:
    l = fib(n)[n-1]
else:
    l = fib(n)[n]
print(l)
