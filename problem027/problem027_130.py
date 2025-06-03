import math


def solve(depth, p1, p2):
    if depth == 0:
        return
    else:
        px = (p2[0] - p1[0]) / 3
        py = (p2[1] - p1[1]) / 3
        s = [p1[0] + px, p1[1] + py]
        t = [p1[0] + 2 * px, p1[1] + 2 * py]
        u = [(t[0] - s[0]) * math.cos(math.pi/3) -
             (t[1] - s[1]) * math.sin(math.pi/3) + s[0],
             (t[0] - s[0]) * math.sin(math.pi/3) +
             (t[1] - s[1]) * math.cos(math.pi/3) + s[1]]
        solve(depth-1, p1, s)
        print(*s)
        solve(depth-1, s, u)
        print(*u)
        solve(depth-1, u, t)
        print(*t)
        solve(depth-1, t, p2)


def main():
    n = int(input())
    print("%f %f" % (0, 0))
    solve(n, [0, 0], [100, 0])
    print("%f %f" % (100, 0))


if __name__ == '__main__':
    main()

