N,D = [int(i) for i in input().split()]
XY = []
count = 0

for i in range(N):
  XY.append([int(i) for i in input().split()])

for xy in XY:
  dd = xy[0]**2+xy[1]**2
  if dd <= D**2:
    count +=1

print(count)