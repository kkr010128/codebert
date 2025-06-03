n, m = map(int, input().split())

def out(s, e):
    while s < e:
        print("{} {}".format(s, e))
        s += 1
        e -= 1

if m % 2 == 0:
    out(1, m)
    out(m + 1, 2 * m + 1)
else:
    out(1, m + 1)
    out(m + 2, 2 * m + 1)