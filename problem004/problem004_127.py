input()
while True:
  try:
    lst = list(map(int,input().split()))
    lst.sort()
    if lst[2] ** 2 == lst[1] ** 2 + lst[0] ** 2:
      print("YES")
    else:
      print("NO")
  except EOFError:
    break
