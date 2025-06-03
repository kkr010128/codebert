import re
S = input()
print('Yes' if len(re.sub(r'hi', '', S)) == 0 else 'No')