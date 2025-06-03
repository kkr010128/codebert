#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 
import collections
import sys
 
 
def count_connected_components(max_v, adj_list):
    result = 0
    visited = collections.defaultdict(bool)
 
    def depth_first_search(start_v):
        visited[start_v] = True
        for v in adj_list[start_v]:
            if not visited[v]:
                depth_first_search(v)
    for u in range(max_v):
        if not visited[u]:
            depth_first_search(u)
            result += 1
    return result
 
 
def main():
    sys.setrecursionlimit(50000)
    n, m = map(int, input().split())
    adj_list = collections.defaultdict(set)
    for _ in range(m):
        a, b = map(lambda x: int(x) - 1, input().split())
        adj_list[a].add(b)
        adj_list[b].add(a)
    print(count_connected_components(n, adj_list) - 1)
 
 
if __name__ == '__main__':
    main()
