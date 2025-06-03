import math

A, B = map(int, input().split())
min1 = math.floor(A * 25/2)
max1 = math.ceil((A + 1) * 25/2)
ans_lis = []
ans1 = False
ans2 = False
for i in range(min1, max1):
  if A == math.floor(i * 2/25):
    ans1 = True
    ans_lis.append(i)
for x in ans_lis:
  if B == math.floor(x * 1/10):
    ans2 = True
    ans = x
    break
if ans1 == True and ans2 == True:
  print(x)
else:
  print(-1)