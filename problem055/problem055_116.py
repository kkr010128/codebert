import sys

official_house = {}
for b in range(1, 5):
    for f in range(1, 4):
        for r in range(1, 11):
            official_house[(b, f, r)] = 0

n = int(sys.stdin.readline())
for line in sys.stdin:
    (b, f, r, v) = [int(i) for i in line.split()]
    official_house[(b, f, r)] += v

for b in range(1, 5):
    if b != 1:
        print("####################")
    for f in range(1, 4):
        for r in range(1, 11):
            print(" %d" % official_house[(b, f, r)], end="")
        print()