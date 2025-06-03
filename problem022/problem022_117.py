# encoding: utf-8


def main():
    n = input()
    t = map(int, raw_input().split())
    q = input()
    s = map(int, raw_input().split())

    sum = 0
    for a in s:
        sum += 1 if a in t else 0

    print sum

main()