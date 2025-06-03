N = int(input())
x = (N+1) * 100 // 108
if x * 108 // 100 == N:
  print(x)
else:
  print(":(")