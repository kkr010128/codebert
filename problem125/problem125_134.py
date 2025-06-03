n = int(input())
for i in range(1, 180, 1):
  if(360*i % n == 0):
    print(int(360*i//n))
    exit(0)