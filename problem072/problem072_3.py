n = int(input())
num_lis = [list(map(int, input().split())) for i in range(n)]
c = 0

for i,j in num_lis:
  if c == 3:
    break
  if i == j:
    c += 1
  else:
    c = 0

if c == 3:
  print("Yes")
else:
  print("No")