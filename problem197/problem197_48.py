from decimal import Decimal

a,b,c = map(str,input().split()) # Decimalを使う場合，文字列で渡す
a_sq = Decimal(a).sqrt()
b_sq = Decimal(b).sqrt()
c_sq = Decimal(c).sqrt()

if a_sq + b_sq < c_sq:
  print("Yes")
else:
  print("No")