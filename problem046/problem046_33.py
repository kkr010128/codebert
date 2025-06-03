from math import pi   # 円周率
# 浮動小数点数で読む
r = float(input())   
area = r * r * pi
cir =(r+r) * pi
print(f'{(area):.6f} {(cir):.6f}')
