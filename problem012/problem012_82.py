def p(x):
 for i in[2,3,5,7,9,11,13,17,19,21,23]:
  if x%i==0:return [1,0][x>i]
 i=29
 while i<=x**.5:
  if x%i==0:return 0
  i+=2
 return 1
n=int(input())
print(sum([p(int(input()))for _ in range(n)]))