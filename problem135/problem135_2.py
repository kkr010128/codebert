import math
arr = input().split( )
a = int(arr[0])
b1, b2 = arr[1].split('.')
b = int(b1)*100 + int(b2)
print(a*b//100)