tmp = input().split(" ")
A = int(tmp[0])
B = int(tmp[1])

if A <= 9 and B <= 9:
  print(A * B)
else:
  print("-1")