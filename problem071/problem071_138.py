a = list(input())
if a[-1] == 's':
  a.append('e')
  a.append('s')
else:
  a.append('s')

print(''.join(a))