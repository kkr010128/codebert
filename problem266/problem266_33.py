N=int(input())
b=0
x = N //100
for y in range(100*x,105*x+1):
  if N==y:
    print(1)
    exit()
print(0)
