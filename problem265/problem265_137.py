from decimal import Decimal
N = int(input())
M = int(N/Decimal(1.08)) + 1
if N == int(M*Decimal(1.08)) :
    print( int(M))
else :
    print(':(')