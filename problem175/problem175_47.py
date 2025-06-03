from itertools import groupby
from statistics import median
from sys import exit

N = int(input())

line = ([(index, v) for index, v in enumerate(input())])


def types(line): return line[1]
def index(line): return line[0]


gp = groupby(sorted(line, key=types), types)

d = {}

for k, v in gp:
    indexes = set([i for i, value in v])
    d[k] = indexes

if 'R' not in d or 'G' not in d or 'B' not in d:
    print(0)
    exit()

delete = 0


for differ in range(1, N):
    for start in range(N):
        if start + differ*2 > N - 1:
            break

        i = line[start]
        j = line[start + differ]
        k = line[start + differ*2]

        if len({i[1], j[1], k[1]}) != 3:
            continue

        upper = max(i[0], j[0], k[0])
        lower = min(i[0], j[0], k[0])
        median_num = median([i[0], j[0], k[0]])
        if upper - median_num == median_num - lower:
            delete += 1

print(len(d['R']) * len(d['G']) * len(d['B']) - delete)
