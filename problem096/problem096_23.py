N,D = (int(x) for x in input().split())
count = 0
for i in range(N):
  x,y = (int(z) for z in input().split())
  dist = x**2 + y**2
  if dist <= D**2:
    count += 1
print(count)