i = list(map(int,input().split()))
if (i[0] == i[1] and i[0] != i[2]) or (i[0] == i[2] and i[0] != i[1])  or (i[1] == i[2] and i[1] != i[0]):
  print("Yes")
else:
  print("No")