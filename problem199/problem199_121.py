import re

S=input()

pattern = '^(hi)+$'

result = re.match(pattern, S)

if result:
	print('Yes')
else:
	print('No')