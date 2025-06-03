n = int(input())
s = 0
for i in range(n):
  x,y = map(int,input().split())
  if x == y:
    s += 1
    if s == 3:
      print("Yes")
      quit()
  else:
    s = 0
print("No")
