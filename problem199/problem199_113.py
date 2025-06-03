import sys
s = input()
if len(s)%2 == 1:
  print('No')
  sys.exit()
for i in range(len(s)//2):
  if s[2*i:2*i+2] != 'hi':
    print('No')
    sys.exit()
print('Yes')
