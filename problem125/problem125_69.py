x = int(input())
for i in range(1, 100000):
  if x * i % 360 == 0:
    print(i)
    exit()
