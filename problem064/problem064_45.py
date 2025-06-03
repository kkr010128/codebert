s = input()
p = input()

s += s[:len(p)-1]
if s.find(p) >= 0:
  print('Yes')
else:
  print('No')