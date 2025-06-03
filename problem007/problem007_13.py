n = int(input())
l = [0 for _ in range(10**4)]
def fib(n):
    if n==0:
      l[0]=1
      return 1
    if n==1:
      l[1]=1
      return 1
    if l[n]!=0:
      return l[n]
    else:
      l[n]=fib(n-1)+fib(n-2)
      return fib(n-1)+fib(n-2)
    
print(fib(n))
