#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def process(commands):
    d = set()
    for c in commands:
        cpair = c.split()
        if cpair[0] == "insert":
            d.add(cpair[1])
        elif cpair[0] == "find":
            r = "yes" if cpair[1] in d else "no"
            print(r)


def main():
    n = int(input())
    commands = [input() for i in range(n)]
    process(commands)


if __name__ == "__main__":
    main()