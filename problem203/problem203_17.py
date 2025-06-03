import math
def abc158c_tax_increase():
    a, b = map(int, input().split())
    for i in range(1001):
        if math.floor(i*0.08) == a and math.floor(i*0.1) == b:
            print(i)
            return
    print('-1')

abc158c_tax_increase()