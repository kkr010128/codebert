import math
debt = 100
for i in range(int(input())):
    debt = math.ceil(debt * 1.05)
print(int(debt) * 1000)