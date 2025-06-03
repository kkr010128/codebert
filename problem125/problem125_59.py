import sys
X = int(input())
for i in range(1,1000):
  if 360*i % X == 0:
    print(360*i//X)
    sys.exit()