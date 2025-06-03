requestMap = list(map(float, input().split()))

D = requestMap[0]
T = requestMap[1]
S = requestMap[2]

dist = S * T

if dist >= D:
  print("Yes")
else:
  print("No")