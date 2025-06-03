S = input()
import re
print('Yes' if re.match(r'^(hi)+$', S) else 'No')
