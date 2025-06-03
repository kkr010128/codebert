X = int(input())

quint = [0] * 1001

for i in range(1, 1001):
  quint[i] = i ** 5
  
for i in range(0, 1001):
  a = X - quint[i] 
  b = X + quint[i]
  try:
    c = quint.index(a)
    print("{} {}".format(c, -i))
    break
  except:
    try:
      c = quint.index(b)
      print("{} {}".format(c, i))
      break
    except:
      continue