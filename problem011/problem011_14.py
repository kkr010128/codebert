#ALDS1_1-B Greatest Common Divisor
def gcd(x,y):
    if x%y == 0:
        print(y)
    else:
        gcd(y,x%y)

x,y = [int(x) for x in input().split()]
if x>y:
    gcd(x,y)
else:
    gcd(y,x)