(A, V) = map(lambda a: float(a), input().split())
(B, W) = map(lambda a: float(a), input().split())
T = float(input())

D = abs(A - B)
X = V - W

if (X*T >= D):
  print("YES")
else:
  print("NO")

