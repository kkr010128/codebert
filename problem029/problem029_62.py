import math

def main():
    x1, y1, x2, y2 = [float(n) for n in input().split()]

    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    print("{:.5f}".format(d));

if __name__ == '__main__':
    main()
