import math
n = int(input())
x = int(n/1.08)

if math.floor(x*1.08) == n:
    print (x)
elif math.floor((x-1)*1.08) == n:
    print (x-1)
elif math.floor((x+1)*1.08) == n:
    print (x+1)
else:
    print (":(")
