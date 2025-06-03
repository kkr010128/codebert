N=int(input())
C=[]
b=0
for x in range(1,N//100+1):
  for y in range(100*x,105*x+1):
    if N==y:
      b=1
  if b==1:
    break
print(b)
