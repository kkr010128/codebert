table = []
i = 0
while True:
  table.append(int(input()))
  if table[i] == 0:
    break
  i += 1

for num in table:
  if num == 0:
    break
  sum = 0
  i = 0
  while num != 0: 
    sum += num % 10
    num //= 10
    if num == 0:
      break
  print(sum)

