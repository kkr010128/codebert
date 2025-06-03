import math

str = input().split(' ')
x1 = float(str[0])
x2 = float(str[1])
y1 = float(str[2])
y2 = float(str[3])

result = (x1-y1)*(x1-y1) + (x2-y2)*(x2-y2)
result = math.sqrt(result) if result != 0 else 0

print('%.6f'%result)