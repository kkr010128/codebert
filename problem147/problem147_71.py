n = input()
nn = input()
nnn = list(nn)
nnn.pop(-1)
nn = "".join(nnn)
if nn == n:
  print("Yes")
else:
  print("No")