#!/usr/bin/env python3
def main():
    from collections import defaultdict

    N = int(input())
    S = [input() for _ in range(N)]

    d = defaultdict(int)
    for s in S:
        d[s] += 1
    
    # d = sorted(d.items())
    d = sorted(d.items(), key=lambda d: d[1], reverse=True)
    res = d[0][1]
    lst = []
    for i in d:
        if res > i[1]:
            break
        lst.append(i[0])
        res = i[1]
    for i in sorted(lst):
        print(i)


if __name__ == '__main__':
    main()
