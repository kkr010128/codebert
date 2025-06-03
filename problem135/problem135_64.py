import math
#A , B = map(float,input().split())
a , b = input().split()
a = int(a)
b = round(100*float(b))

#ans = int (A *(B*100)/100)  
print(a*b//100)
