n = int(raw_input())

output = ""
for i in range(1, n + 1):
  x = i
  if x % 3 == 0:
    output += " "
    output += str(i)
    continue

  while True:
    if x % 10 == 3:
      output += " "
      output += str(i)
      break
    else:
      x /= 10
      if x == 0:
        break
print output