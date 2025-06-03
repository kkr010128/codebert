a = 100000
b = 1000
for i in range(input()):
    a *= 1.05
    if a % b > 0:
        a = a - a % b + b
print int(a)