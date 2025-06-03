a, b, c = [int(i) for i in input().split(" ")]
 
ab = a == b
bc = b == c
ca = c == a
 
cnt = 0
for r in [ab, bc, ca]:
  if r:
    cnt += 1

if cnt == 1:
  print("Yes")
else:
  print("No")