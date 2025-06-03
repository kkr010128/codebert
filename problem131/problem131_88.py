import sys

a, v = map(int, input().split())
b, w = map(int, input().split())
t = int(input())

if v <= w:
  print('NO')
  sys.exit()

a_b_dist = abs(a-b)
v_w_dist = abs(v-w)

if v_w_dist * t < a_b_dist:
  print('NO')
  sys.exit()

print('YES')
