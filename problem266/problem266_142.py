N = int(input())
x = N // 100
y = N % 100
if y <= 5 * x:
  print(1)
else:
  print(0)