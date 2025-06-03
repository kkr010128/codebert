from decimal import Decimal 
a,b,c = map(int,input().split())
d = Decimal(0.5)
ans = "Yes" if a**d + b**d < c**d else "No"
print(ans)