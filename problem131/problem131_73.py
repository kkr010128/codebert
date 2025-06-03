A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())
if V == W:
  print("NO")
  exit()
if A > B:
  t1 = A
  A = B
  B = t1
if V < W:
#  print("A")
  print("NO")
  exit()
if (A + V*T) - (B + W*T) >= 0:
  print("YES")
  exit()
else:
  print("NO")
  exit()