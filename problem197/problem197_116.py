from decimal import Decimal as de
a,b,c=map(de,input().split())
print('Yes' if a**de('0.5')+b**de('0.5')<c**de('0.5') else 'No')