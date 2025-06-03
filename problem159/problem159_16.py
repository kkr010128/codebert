from decimal import Decimal
import math

def main():
    x = Decimal(input())
    y = 0
    p = Decimal(100)
    gr = Decimal('1.01')
    while p < x:
        p *= gr 
        p = math.floor(p) 
        y += 1

    print(y)

main()
