from math import sqrt
def distance2(x, y, p='infinite'):
    if p == 'infinite':
        return max([abs(dx - dy) for dx, dy in zip(x,y)])
    else:
        return sum([(abs(dx - dy)**p) for dx, dy in zip(x, y)])**(1/p)

if __name__ == '__main__':
    n = int(input())
    x = list(map(int, input().split()))[0:n]
    y = list(map(int, input().split()))[0:n]
    print(distance2(x, y, 1))
    print(distance2(x, y, 2))
    print(distance2(x, y, 3))
    print(distance2(x, y))

