def north(d):
    d[0], d[1], d[5], d[4] = d[1], d[5], d[4], d[0]


def west(d):
    d[0], d[2], d[5], d[3] = d[2], d[5], d[3], d[0]


def east(d):
    d[0], d[3], d[5], d[2] = d[3], d[5], d[2], d[0]


def south(d):
    d[0], d[4], d[5], d[1] = d[4], d[5], d[1], d[0]


F = {'N': north, 'W': west, 'E': east, 'S': south}

d, os = list(map(int, input().split())), input()

for o in os:
    F[o](d)

print(d[0])