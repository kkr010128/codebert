s = input()
li = list(s)

if sum([int(n) for n in li]) % 9 == 0:
  print("Yes")
else:
  print("No")