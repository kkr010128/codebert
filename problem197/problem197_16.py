from decimal import Decimal as d
a,b,c=input().split()
print('Yes'if d(a)**d('0.5')+d(b)**d('0.5')<d(c)**d('0.5')else'No')