from math import floor
n = int(input())

def debt(week):
    debt = 100000
    for i in range(1,n+1):
        debt *= 1.05
        amari = debt % 1000
        if amari:
            debt += 1000 - amari
    return int(debt)

print(debt(n))