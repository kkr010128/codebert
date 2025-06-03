N,D = map(int,input().split())

count = 0

for i in range(N):
  x,y = map(int,input().split())
  
  if x**2+y**2 <= D**2:
    count = count + 1
  else:
    count = count + 0

print(count)