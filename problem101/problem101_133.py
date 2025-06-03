a, b, c = map(int, input().split())
k = int(input())
r = 0
while b <= a :
  b = 2 * b
  r += 1
while c <= b:
  c = 2 * c
  r += 1
if r <= k:
  print("Yes")
else:
  print("No")