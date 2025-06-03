count = 0
for i in range(10000):
  a = input()
  a = int(a)
  if a >= 1:
    count += 1
    print('Case '+str(count)+': '+str(a))
  else:
    break

