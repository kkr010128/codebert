A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())
d = abs(A-B)
if d-(V-W)*T<=0:
  print("YES")
else:
  print("NO")