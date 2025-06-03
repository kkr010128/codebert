import re
s = input()
if re.sub(r'hi', '', s) == '':
    print('Yes')
else:
    print('No')
