import re
S = input()
rds = list(map(lambda x: len(x), re.findall('R{1,}', S)))
print(max(rds)) if rds else print(0)
