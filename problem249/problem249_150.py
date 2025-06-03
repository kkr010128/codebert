A, B, K = list(map(lambda x: int(x), input().split(" ")))
if A >= K:
  print(str(A - K) + " " + str(B))
elif A + B >= K:
  print("0 " + str(A + B - K))
else:
  print("0 0")