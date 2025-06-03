n = int(input())

if n%2 == 0:
  print(float((n//2)/n))
elif n == 1:
  print(float(1))
else:
  print(float((n//2 + 1)/n))