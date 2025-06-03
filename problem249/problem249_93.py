a, b, k = map(int, input().split())

if a >= k:
  c = a-k
  e = "{0} {1}".format(c, b)
  print(e)
  
elif a < k <= a + b:
  c = b + a - k
  e = "{0} {1}".format(0, c)
  print(e)

else:
  print('0' +' ' +  '0')


