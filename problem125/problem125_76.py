import math

if __name__ == "__main__":
    deg = int(input())
    print(360//math.gcd(deg, 360))