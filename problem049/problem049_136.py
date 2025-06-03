H = ''
W = ''
i = j = 0

while True:
  line = input()
  line = line.split()
  H = int(line[0])
  W = int(line[1])

  if H == 0 and W == 0:
    break

  while i < H:
    print('#'*W)
    i += 1
  i = 0
  print()