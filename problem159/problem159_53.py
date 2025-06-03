from decimal import Decimal
X=int(input())

c =Decimal(100)
C=0
while c<X:
  c=Decimal(c)*(Decimal(101))//Decimal(100)
  C+=1
print(C)