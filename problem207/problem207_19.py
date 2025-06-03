a = []
for i in range(3):
  t = [int(x) for x in input().split()]
  a.append(t)
n = int(input())
b = [int(input()) for i in range(n)]
m = [[0 for j in range(3)] for i in range(3)]
for i in range(3):
  for j in range(3):
    for k in b:
      if (a[i][j] == k):
        m[i][j] = 1
for i in range(3):
  if (m[i][0] and m[i][1] and m[i][2]):
    print("Yes")
    exit()
for i in range(3):
  if (m[0][i] and m[1][i] and m[2][i]):
    print("Yes")
    exit()
if ((m[0][0] and m[1][1] and m[2][2]) or (m[0][2] and m[1][1] and m[2][0])):
  print("Yes")
  exit()
print("No")