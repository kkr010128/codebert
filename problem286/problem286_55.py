def getList():
    return list(map(int, input().split()))
a, b = getList()
if a > 9 or b > 9:
  print(-1)
else:
  print(a*b)