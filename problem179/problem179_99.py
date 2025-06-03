x, y = map(int, input().split())
l = list(map(int, input().split()))
count = 0

for i in range(x):
  if l[i] >= sum(l)*(1/(4*y)):
    count += 1
    
if count >= y:
  print("Yes")
else:
  print("No")