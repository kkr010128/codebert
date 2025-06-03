s = input()
if 4 < len(s) < 6:
  print('No')
  exit()

if s[::-1] != s:
  print('No')
  exit()
s = s[:len(s)//2]
if s[::-1] != s:
  print('No')
  exit()
print('Yes')