ans = []

while True:
  cin = raw_input().split()
  a = int(cin[0])
  b = int(cin[2])
  if cin[1] == "+":
    ans.append(a + b)
  elif cin[1] == "-":
    ans.append(a - b)
  elif cin[1] == "*":
    ans.append(a * b)
  elif cin[1] == "/":
    ans.append(a // b)
  elif cin[1] == "?":
    break

for i in range(len(ans)):
  print(ans[i])