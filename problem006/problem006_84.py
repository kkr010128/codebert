import math

def calc_debt(week=0):
    debt = 100000
    for i in range(week):
        debt = int(math.ceil(debt * 1.05 / 1000))*1000
    return debt 

print(calc_debt(int(input())))