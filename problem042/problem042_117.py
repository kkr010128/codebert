l = []
while True:
  i = str(input())
  if i == '0':
    break
  else:
    l.append(i)
t = 0
for i in l:
  t += 1
  print('Case '+str(t)+': '+i)
