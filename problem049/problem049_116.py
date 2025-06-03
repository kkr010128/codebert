h = -1
w = -1

while (h != 0) and (w != 0):
  input = map(int, raw_input().split(" "))
  h = input[0]
  w = input[1]
  if (h == 0 and w == 0):
    break

  i = 0
  j = 0
  line = ""

  while j < w:
    line += "#"
    j += 1

  while i < h:
    print line
    i += 1

  print ""