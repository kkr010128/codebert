N = int(input())
f = 0
for i in range(9, 0, -1):
  if N % i == 0 and N / i <= 9:
    print("Yes")
    f = 1
    break
if f == 0:
  print("No")