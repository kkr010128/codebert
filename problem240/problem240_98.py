import sys


def resolve(in_):
    N, M = map(int, next(in_).split())
    PS = tuple(line.strip().split() for line in in_)
    
    ac = set()
    wa = {}

    for p, s in PS:
        if s == 'AC':
            ac.add(p)
        if s == 'WA' and p not in ac:
            wa[p] = wa.setdefault(p, 0) + 1

    penalties = 0
    for k, v in wa.items():
        if k in ac:
            penalties += v
    
    return '{} {}'.format(len(ac), penalties)


def main():
    answer = resolve(sys.stdin)
    print(answer)


if __name__ == '__main__':
    main()
