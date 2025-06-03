a = [[0] * 3 for x in range(3)]
s = [[0] * 3 for x in range(3)]
for i in range(3):
  a[i] = [int(x) for x in input().split()]
n = int(input())
b = []
for i in range(n):
  b.append(int(input()))
for i in range(n):
  for j in range(3):
    for k in range(3):
      if b[i] == a[j][k]:
        s[j][k] = 1
res = "No"
if s[0][0] == 1 and s[0][1] == 1 and s[0][2] == 1:
  res = "Yes"
if s[1][0] == 1 and s[1][1] == 1 and s[1][2] == 1:
  res = "Yes"
if s[2][0] == 1 and s[2][1] == 1 and s[2][2] == 1:
  res = "Yes"
if s[0][0] == 1 and s[1][0] == 1 and s[2][0] == 1:
  res = "Yes"
if s[0][1] == 1 and s[1][1] == 1 and s[2][1] == 1:
  res = "Yes"
if s[0][2] == 1 and s[1][2] == 1 and s[2][2] == 1:
  res = "Yes"
if s[0][0] == 1 and s[1][1] == 1 and s[2][2] == 1:
  res = "Yes"
if s[2][0] == 1 and s[1][1] == 1 and s[0][2] == 1:
  res = "Yes"
print(res)