#!/usr/bin/env python
from __future__ import division, print_function
from sys import stdin
from Queue import Queue
 
 
def main():
    num = int(stdin.readline())
 
    L = []
    for _ in xrange(num):
        L.append([int(s) for s in stdin.readline().split()[2:]])
 
    d = [-1] * num
    d[0] = 0
    q = Queue(100)
    q.put(0)
    while not q.empty():
        u = q.get()
        for v in L[u]:
            if d[v-1] < 0:
                d[v-1] = d[u] + 1
                q.put(v-1)
 
    for i, v in enumerate(d):
        print(i+1, v)
 
 
main()