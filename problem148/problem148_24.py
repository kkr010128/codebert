def Qb():
    a, b, c, k = map(int, input().split())

    ra = min(k, a)
    k -= ra
    k -= b
    rc = 0 if k <= 0 else -(min(k, c))
    print(ra + rc)


if __name__ == '__main__':
    Qb()
