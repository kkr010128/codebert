import re
s = input()
s = re.sub('hi','0',s)
s = re.sub('0','',s)
if s == '':
    print('Yes')
else:
    print('No')