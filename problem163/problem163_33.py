tmp = input().split(" ")
S = int(tmp[0])
W = int(tmp[1])

if S <= W:
  print("unsafe")
else:
  print("safe")