n = int(input())

for i in range(9,0,-1):
  if n % i == 0:
    work = n / i
    if work < 10:
      print("Yes")
      break
    else:
      print("No")
      break