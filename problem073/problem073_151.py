n=int(input())
  
def f(i):
  if n%i==0:
    return n//i-1
  else:
    return n//i

sum=0
for i in range(1,n):
  sum+=f(i)

print(sum)