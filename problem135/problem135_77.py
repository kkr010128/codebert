import math
a,b = map(str, input().split())
b = b.replace(".","")
a = int(a)
b = int(b)
print(a * b // 100)