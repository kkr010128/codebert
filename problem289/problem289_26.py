import math
def at(x):
    return math.degrees(math.atan(x))

a, b, x = map(int, input().split())
print(at(a*b*b/(2*x)) if 2*x < a*a*b else at(2*(a*a*b-x)/(a**3)))