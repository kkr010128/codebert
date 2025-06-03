from sys import stdin

for l in stdin:
    l = l.rstrip()
    if 0 == int(l):
        break

    print(sum([int(ch) for ch in l]))