import math


class vec2d(object):
    def __init__(self, x, y) -> None:
        self.x = float(x)
        self.y = float(y)

    def rot(self, theta: float):
        newx = self.x * math.cos(theta) - self.y * math.sin(theta)
        newy = self.x * math.sin(theta) + self.y * math.cos(theta)
        return vec2d(newx, newy)

    def __str__(self):
        return ' '.join(map(str, [self.x, self.y]))

    def __format__(self, format_spec):
        return ' '.join(map(lambda x: format(x, format_spec), [self.x, self.y]))

    def __add__(self, other):
        return vec2d(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return vec2d(self.x - other.x, self.y - other.y)

    def __mul__(self, k):
        return vec2d(self.x * k, self.y * k)

    def __truediv__(self, k):
        return self.__mul__(1 / k)

    def prod(self, other):
        return self.x * other.x + self.y * other.y


def cochcurve(p1, p2, n):
    if n > 0:
        pd = (p2 - p1) / 3
        ps = p1 + pd
        pu = ps + pd.rot(math.pi / 3)
        pt = ps + pd
        cochcurve(p1, ps, n-1)
        print(f'{ps:>12.6f}')
        cochcurve(ps, pu, n-1)
        print(f'{pu:>12.6f}')
        cochcurve(pu, pt, n-1)
        print(f'{pt:>12.6f}')
        cochcurve(pt, p2, n-1)


n = int(input())
S = vec2d(0, 0)
T = vec2d(100, 0)
print(f'{S:>12.6f}')
cochcurve(S, T, n)
print(f'{T:>12.6f}')
