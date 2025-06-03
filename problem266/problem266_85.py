# C - 100 to 105
# https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_c

x = int(input())
d, m = divmod(x, 100)

D = [0] * 5

for i in range(4, -1, -1):
  D[i], m = divmod(m, i + 1)

if d >= sum(D):
  print(1)
else:
  print(0)