def p(x):
 i=2
 while i<=x**.5:
  if x%i==0:return 0
  i+=1
 return 1
n=int(input())
print(sum([p(int(input()))for _ in range(n)]))