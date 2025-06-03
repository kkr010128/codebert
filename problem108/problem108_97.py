import math
N =int(input())

s = N / 1000

if s == 0 :
    print(0)
else :
    a = math.ceil(s) * 1000 - N
    print(int(a))