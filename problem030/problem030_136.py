import math

def main():
    a, b, ang_ab = [float(x) for x in input().split()]

    rad_ab = (ang_ab/180)*math.pi
    c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(rad_ab))

    h = b*math.sin(rad_ab)
    s = (a*h)/2
    l = a+b+c

    print("{:f} {:f} {:f}".format(s, l, h))

if __name__ == '__main__':
    main()

