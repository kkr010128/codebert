A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())
if not V > W:
  print("NO")
elif (V-W)*T >= abs(B-A):
  print("YES")
else:
  print("NO")
