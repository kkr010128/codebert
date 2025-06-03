# encording: utf-8

_ = int(input())
ns = [int(e) for e in input().split()]
_ = int(input())
qs = [int(e) for e in input().split()]


def main(ns, qs):
    total = 0
    for q in qs:
        if q in ns:
            total += 1
    return total


print(main(ns, qs))