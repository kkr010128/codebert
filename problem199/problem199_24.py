import sys
s = input()
a = ''
n = len(s)
if (n%2) != 0:
    print('No')
    sys.exit()

i = 0
while (n-i) > 0:
    if s[i:i+2] == ('hi'):
        i += 2
    else:
        print('No')
        sys.exit()
print('Yes')