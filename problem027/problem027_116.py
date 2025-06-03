import cmath

cmp_s = cmath.rect(1/3, 0)
cmp_u = cmath.rect(3**(-1/2), cmath.pi / 6)
cmp_t = cmath.rect(2/3, 0)


def koch_curve(p1: complex, p2: complex, n):
    if n != 0:
        cmp = p2 - p1
        s, u, t = [p1 + cmp * c for c in (cmp_s, cmp_u, cmp_t)]
        koch_curve(p1, s, n-1)
        print('{0:8f} {1:8f}'.format(s.real, s.imag))
        koch_curve(s, u, n-1)
        print('{0:8f} {1:8f}'.format(u.real, u.imag))
        koch_curve(u, t, n-1)
        print('{0:8f} {1:8f}'.format(t.real, t.imag))
        koch_curve(t, p2, n-1)


def main():
    n = int(input())
    print('{0:8f} {1:8f}'.format(.0, .0))
    koch_curve(complex(.0, .0), complex(100.0, .0), n)
    print('{0:8f} {1:8f}'.format(100.0, .0))


if __name__ == '__main__':
    main()

