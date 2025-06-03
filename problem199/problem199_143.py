s = input()
while s[:2] == 'hi':
    s = s[2:]
if s == '': print('Yes')
else: print('No')