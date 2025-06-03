import decimal

def main():
    
    
    A, B = map(decimal.Decimal,input().split())
    
    if A == 0:
        return 0

    else:
        AB = A*B
        return int(AB)
        
    
print(main())