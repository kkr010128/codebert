# print(max([len(v) for v in input().split('S')]))

d = {
    'RRR': 3,
    'RRS': 2,
    'RSR': 1,
    'RSS': 1,
    'SRR': 2,
    'SRS': 1,
    'SSR': 1,
    'SSS': 0,
}
print(d[input()])
