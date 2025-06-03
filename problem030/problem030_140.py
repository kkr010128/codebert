# -*-coding:utf-8

import math

def main():

    a, b, degree = map(int, input().split())

    radian = math.radians(degree)

    S = 0.5*a*b*math.sin(radian)
    x = a + b + math.sqrt(pow(a,2)+pow(b,2)-2*a*b*math.cos(radian))
    print('%.8f' % S)
    print('%.8f' % x)
    print('%.8f' % ((2*S)/a))



if __name__ == '__main__':
    main()