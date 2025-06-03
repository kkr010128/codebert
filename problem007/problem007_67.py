F = {}

def fib(n):
  global F
  if n < 0:
    print("error")
    exit()
  if n < 2:
    F[n] = 1
    return F[n]
#  F[n] = fib(n-1) + fib(n-2)
  F[n] = F[n-1] + F[n-2]
  return F[n]

n = int(input())
#print(fib(n))
#n = int(input())
#print(fib(n))
#fib(44)
for i in range(n+1):
  result = fib(i)
print(result)
#  print(F[i])