import re
num = list(map(int, re.split('\s+', input())))
print(num[0] * num[1], end=" ")
print((num[0] + num[1]) * 2)