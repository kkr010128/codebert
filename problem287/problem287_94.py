N = int(input())

for i in range(1,10):
  for j in range(1,10):
    temp = i*j
    if N == temp:
      print("Yes")
      exit()
print("No")