n = (int)(input())
base = (int)(n**(1/2))
a=0
b=0
for i in range(base, 0, -1):
  if n % i == 0:
    a = i
    b = n // i
    break
#print(a,b)
print(a + b - 2)