from math import cos, sin, pi


def make_koch_curve(N, n1, n2):
    s = ((2 * n1[0] + n2[0]) / 3, (2 * n1[1] + n2[1]) / 3)
    t = ((n1[0] + 2 * n2[0]) / 3, (n1[1] + 2 * n2[1]) / 3)
    u = ((t[0] - s[0])*cos(pi/3) - (t[1] - s[1])*sin(pi/3) + s[0],
         (t[0] - s[0])*sin(pi/3) + (t[1] - s[1])*cos(pi/3) + s[1])
    if N == 0:
        return
    make_koch_curve(N-1, n1, s)
    print(*s)
    make_koch_curve(N-1, s, u)
    print(*u)
    make_koch_curve(N-1, u, t)
    print(*t)
    make_koch_curve(N-1, t, n2)


def main():
    N = int(input())
    n1 = (0., 0.)
    n2 = (100., 0.)
    print(*n1)
    make_koch_curve(N, n1, n2)
    print(*n2)


if __name__ == '__main__':
    main()

