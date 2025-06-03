a, b, c = map(int, input().split())
k = int(input())
 
for i in range(k):
  if a < b < c:
    break
  elif b <= a:
    b = b*2
  elif c <= b:
    c = c*2
 
if a < b < c:
  print("Yes")
else:
  print("No")