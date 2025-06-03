import math
shuu = input()
num = int(shuu)
ganpon = 100000
i = 1
while i <= num:
    ganpon *= 1.05
    ganpon /= 1000
    ganpon = math.ceil(ganpon)
    ganpon *= 1000
    i += 1
    pass
#ganpon /= 1000
#ganpon = math.ceil(ganpon)
#ganpon *= 100000
print(ganpon)