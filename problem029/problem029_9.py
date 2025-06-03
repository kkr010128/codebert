import math

if __name__ == '__main__':
    x1, y1, x2, y2 = [float(i) for i in input().split()]
    d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    print("{0:.5f}".format(d))