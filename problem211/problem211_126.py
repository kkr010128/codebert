import fileinput

n, r = map(int, input().split())

if n >= 10:
    print(r)
else:
    rr = r + 100 * (10 - n)
    print(rr)

