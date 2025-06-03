str = input()
num = int(str)
if num % 2 == 0:
  print('-1');
else:
  i = 1
  j = 7
  while j % num != 0 and i <= num:
    j = (j % num) * 10 + 7
    i += 1
  if i > num:
    print('-1');
  else:
    print(i);
  
