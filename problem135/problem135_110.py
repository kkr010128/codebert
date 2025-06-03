from decimal import Decimal
from math import floor

def main():
    a, b = map(Decimal,input().split())
    
    print(floor(a*b))
    
main()