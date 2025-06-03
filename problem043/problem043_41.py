# coding=utf-8

while True:
    x, y = map(int, raw_input().rstrip().split())
    if x + y:
        print '{} {}'.format(*sorted([x, y]))
    else:
        break