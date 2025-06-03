A, V = list(map(int, input().split()))
B, W = list(map(int, input().split()))
T = int(input())

abs_BA = abs(B-A)
sub_VW = V - W

if sub_VW <= 0:
  print("NO")
elif abs_BA <= T * sub_VW:
  print("YES")
else:
  print("NO")