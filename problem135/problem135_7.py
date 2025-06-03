from decimal import Decimal
A,B=input().split()
A=int(A)
B=Decimal(B)
Bint=int(B)
B1=int((B-Bint)*100)
result=A*Bint+A*B1//100
print(result)