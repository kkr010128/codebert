N = int(input())
d = [0] * N
c = 0
b = True
for i in range(N):
  d[i] = list(map(int, input().split()))
  if d[i][0] == d[i][1]:
    c += 1
    b = True
  else:
    c = 0
    b = False
  if c == 3:
    break
if c == 3:
  print("Yes")
else:
  print("No")