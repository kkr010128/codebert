s = list(input())

a = 0
b = 0
c = 0

for i in range(len(s)):
  if i%2 == 0 and s[i] == "h":
    a += 1
  elif i%2 == 1 and s[i] == "i":
    b += 1
  else:
    c += 1
    
if a == b and c == 0:
  print('Yes')
else:
  print('No')