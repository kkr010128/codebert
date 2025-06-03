while True:
  x = input().rstrip('\r\n')
  if x == '0':
    break

  sum = 0

  for ii in range(len(x)):
    sum += int(x[ii])
  print(sum)

