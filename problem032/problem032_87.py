import math

def minkowski(x, y, p):
    if p == 0:
        return max(map(lambda xi,yi: abs(xi-yi), x, y))
    else:
        return math.pow(sum(map(lambda xi,yi: math.pow(abs(xi-yi), p), x, y)), 1/p)

if __name__ == '__main__':
    n = int(input())
    x = [int(i) for i in input().split()]
    y = [int(i) for i in input().split()]
    print("{0:.6f}".format(minkowski(x, y, 1)))
    print("{0:.6f}".format(minkowski(x, y, 2)))
    print("{0:.6f}".format(minkowski(x, y, 3)))
    print("{0:.6f}".format(minkowski(x, y, 0)))