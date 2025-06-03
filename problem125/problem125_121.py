import math
print([ ( int(x) * 360 // math.gcd(int(x),360) ) // int(x) for x in input().split(' ') ][0])