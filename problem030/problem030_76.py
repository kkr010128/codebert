import math

def triangle(a, b, deg):
    result = {}
    rad = math.radians(deg)
    c = math.sqrt(a*a+b*b-(2*a*b*math.cos(rad)))
    s = (a+b+c)/2
    result['area'] = math.sqrt(s*(s-a)*(s-b)*(s-c))
    result['perimeter'] = a+b+c
    result['height'] = result['area'] * 2 / a
    return result

if __name__ == '__main__':
    a, b, deg = map(int, input().split())
    triangle = triangle(a, b, deg)
    print(triangle['area'])
    print(triangle['perimeter'])
    print(triangle['height'])

