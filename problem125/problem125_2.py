x = int(input())
for i in range(1,1000):
  if (360*i)%x == 0:
    print((360*i)//x)
    exit()