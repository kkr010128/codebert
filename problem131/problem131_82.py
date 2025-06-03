A, V = map(int, input().split())
B, W = map(int, input().split())
T    = int(input())

set_position = abs(B-A)
move         = V-W

if move*T >= set_position:
  print("YES")
else:
  print("NO")