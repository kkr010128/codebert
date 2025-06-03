class Point:
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y


def solve(p1, p2):
    s_x = p1.x + (p2.x - p1.x) * (1/3)
    s_y = p1.y + (p2.y - p1.y) * (1/3)
    t_x = p1.x + (p2.x - p1.x) * (2/3)
    t_y = p1.y + (p2.y - p1.y) * (2/3)
    u_x = (p2.x + p1.x) * (1/2) + (p1.y - p2.y) * (1/6) * pow(3, 1/2)
    u_y = (p2.y + p1.y) * (1/2) + (p2.x - p1.x) * (1/6) * pow(3, 1/2)
    s = Point(s_x, s_y)
    t = Point(t_x, t_y)
    u = Point(u_x, u_y)
    return [s, u, t]


if __name__ == "__main__":
    n = int(input())
    P = [Point(0, 0), Point(100, 0)]
    for i in range(n):
        TMP = []
        for j in range(len(P) - 1):
            TMP.append(P[j])
            TMP += solve(P[j], P[j+1])
        TMP.append(P[-1])
        P = TMP

    for p in P:
        print('{} {}'.format(p.x, p.y))

