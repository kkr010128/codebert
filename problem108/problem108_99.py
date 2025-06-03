n = int(input())
if n % 1000 == 0:
  if n > 1000:
  	print(0)
  else:
    print(1000 - n)
else:
  k = n % 1000
  print(1000 - k)