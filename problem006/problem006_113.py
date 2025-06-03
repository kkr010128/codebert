import math
while True:
    try:
        n=input()
        x=100000
        for i in xrange(n):
            x=math.ceil(x*1.05/1000)*1000
        print(int(x))
    except EOFError: break