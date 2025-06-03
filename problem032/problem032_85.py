from math import sqrt

def g():
    _ = input()
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))

    f1 = lambda it: abs(it[0]-it[1])
    f2 = lambda it: (it[0]-it[1]) ** 2
    f3 = lambda it: abs(it[0]-it[1]) ** 3

    yield sum(map(f1, zip(x, y)))
    yield sqrt(sum(map(f2, zip(x, y))))
    yield sum(map(f3, zip(x, y))) ** (1/3)
    yield max(map(f1, zip(x, y)))

for n in g():
    print("{:.6f}".format(n))