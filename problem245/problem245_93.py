import re

N = int(input())
S = input()

result = re.findall(r'ABC', S)

print(len(result))
