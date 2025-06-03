#!/usr/bin/env python
#-*- coding: utf-8 -*-


class Queue:
    def __init__(self):
        self.l = []

    def enqueue(self, x):
        self.l.append(x)

    def dequeue(self):
        x = self.l[0]
        del self.l[0]
        return x

    def is_empty(self):
        return len(self.l) == 0


class Process:
    def __init__(self, name, time):
        self.name = name
        self.time = time


if __name__ == '__main__':
    n, q = map(int, raw_input().split())
    Q = Queue()
    i = 0
    while i != n:
        tmp = raw_input().split()
        Q.enqueue(Process(tmp[0], int(tmp[1])))
        i += 1
    cnt = 0
    while not Q.is_empty():
        p = Q.dequeue()
        if p.time > q:
            p.time -= q
            cnt += q
            Q.enqueue(p)
        else:
            cnt += p.time
            print p.name, cnt
