n = input()
a, b = 0, 100
for i in n:
  j = int(i)
  a, b = min(a+j,b+j), min(a+11-j,b+9-j)
  if j == 0:
    b = a+100
print(min(a,b))