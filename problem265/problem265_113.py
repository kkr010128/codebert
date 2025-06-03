N = int(input())
for i in range(50000):
  if N <= i*1.08 < N + 1:
    print(i)
    break
else:
  print(":(")
