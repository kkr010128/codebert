s = ''
while True:
  try:
    s += input().lower()
  except EOFError:
    break
for i in range(97, 123):
  print(chr(i)+' : '+str(s.count(chr(i))))
