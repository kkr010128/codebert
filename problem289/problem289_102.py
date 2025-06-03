import math

def main():
    a, b, x = map(int, input().split())
    V = a**2 * b
    if x <= V/2:
        rad = math.atan(a * b**2 / (2*x))
        print(math.degrees(rad))
    else:
        rad = math.atan(2 * (a**2 * b - x) / a**3)
        print(math.degrees(rad))    
main()