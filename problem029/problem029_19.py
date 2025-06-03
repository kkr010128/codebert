import math
a,b,c,d=map(float,input().split())
x=math.sqrt((a-c)**2 + (b-d)**2)
print(round(x,8))
 #round(f,6)でfを小数点以下6桁にまとめる。
