import re

c = input()
p = '^.{2}(.)\\1(.)\\2$'
print('Yes' if re.match(p, c) else 'No')