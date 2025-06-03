n = int(input())
count = 0


for i in range(0, n):
  tmp = input()
  if tmp.split()[0] == tmp.split()[1]:
    count += 1
    if count == 3:
        break
  else:
    count = 0


if count == 3:
  print('Yes')
else:
  print('No')