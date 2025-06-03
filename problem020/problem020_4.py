#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import collections


def process(commands):
    queue = collections.deque()
    for c in commands:
        if "insert" in c:
            queue.appendleft(int(c[7:]))
        elif "deleteFirst" in c:
            try:
                _ = queue.popleft()
            except IndexError as e:
                pass
        elif "deleteLast" in c:
            try:
                _ = queue.pop()
            except IndexError as e:
                pass
        elif "delete" in c:
            try:
                queue.remove(int(c[7:]))
            except ValueError as e:
                pass
    print(" ".join(list(map(str, queue))))


def main():
    n = int(input())
    process([input() for i in range(n)])


if __name__ == "__main__":
    main()