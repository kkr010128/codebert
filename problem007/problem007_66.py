def fib(n):
  if n==0 or n==1:
    return 1
  
  x=[1,1]
  for i in range(2,n+1):
    x.append(x[i-1]+x[i-2])

  return x[-1]

print(fib(int(input())))

