s = input()

if s[0] == "S":
  if s[1] == "S":
    if s[2] == "S":
      print("0")
    else:
      print("1")
  if s[1] == "R":
    if s[2] == "S":
      print("1")
    else:
      print("2")
if s[0] == "R":
  if s[1] == "S":
    if s[2] == "S":
      print("1")
    else:
      print("1")
  if s[1] == "R":
    if s[2] == "S":
      print("2")
    else:
      print("3")