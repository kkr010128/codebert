import math
SIN_T = math.sin(math.pi / 3)
COS_T = math.cos(math.pi / 3)


def koch(p0, p4):
    p1 = ((p0[0]*2 + p4[0])/3, (p0[1]*2 + p4[1])/3)
    p3 = ((p0[0] + p4[0]*2)/3, (p0[1] + p4[1]*2)/3)
    p2 = (COS_T*(p3[0]-p1[0]) + -SIN_T*(p3[1]-p1[1]) + p1[0],
          SIN_T*(p3[0]-p1[0]) + COS_T*(p3[1]-p1[1]) + p1[1])

    return [p1, p2, p3, p4]


if __name__ == "__main__":
    n = int(input())
    points = [(0, 0), (100, 0)]

    for _ in [0]*n:
        _points = [points[0]]
        for origin, dest in zip(points, points[1:]):
            _points += koch(origin, dest)

        points = _points

    for p in points:
        print(*p)
