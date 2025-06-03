import re

s = re.sub('(hi)+','',input())

print('No' if s else 'Yes')