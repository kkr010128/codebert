A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())

if abs(A-B) - (V-W)*T <= 0:
  print("YES")
elif A==B:
  print("YES")
else:
  print("NO")