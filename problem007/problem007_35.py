n = int(input())
def fib(i):
    if i<=1: return 1
    else: 
     a=0
     b=1
     for i in range(n+1):
      c=b+a
      b=a
      a=c
     return c
print(fib(n))
