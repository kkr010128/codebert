import sys
X = int(input())

for i in range(1,180):
  if int(360*i/X) == 360*i/X:
    print(int(360*i/X))
    sys.exit()