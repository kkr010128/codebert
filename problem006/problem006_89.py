import math
result = 100000
for i in range(int(input())):
    result *= 1.05
    result = math.ceil(result/1000)*1000
print(result)