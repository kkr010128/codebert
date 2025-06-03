#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

input:
6
1 2 2 3
2 2 3 4
3 1 5
4 1 6
5 1 6
6 0

output:
1 1 12
2 2 11
3 3 8
4 9 10
5 4 7
6 5 6

"""
import sys

UNVISITED, VISITED_IN_STACK, POPPED_OUT = 0, 1, 2


def dfs(v_init):
    global timer

    # init the first node of overall graph iterations(times >= 1)
    stack = list()
    stack.append(v_init)
    d_time[v_init] += timer
    # init end

    while stack:
        current = stack[-1]
        v_table = adj_table[current]
        visited[current] = VISITED_IN_STACK
        # if adj is None, current's adj(s) have been all visited
        adj = v_table.pop() if v_table else None

        if adj:
            if visited[adj] is UNVISITED:
                visited[adj] = VISITED_IN_STACK
                timer += 1
                d_time[adj] += timer
                stack.append(adj)
        else:
            stack.pop()
            visited[current] = POPPED_OUT
            timer += 1
            f_time[current] += timer

    return None


def dfs_init():
    global timer
    for v in range(v_num):
        if visited[v + 1] == UNVISITED:
            dfs(v + 1)
            timer += 1


if __name__ == '__main__':
    _input = sys.stdin.readlines()
    v_num = int(_input[0])
    vertices = map(lambda x: x.split(), _input[1:])

    # config length = (v_num + 1)
    # stack = []
    visited = [UNVISITED] * (v_num + 1)
    d_time, f_time = ([0] * (v_num + 1) for _ in range(2))
    adj_table = tuple([] for _ in range(v_num + 1))
    for v_info in vertices:
        v_index, adj_num, *adj_list = map(int, v_info)
        # assert len(adj_list) == adj_num
        adj_table[v_index].extend(sorted(adj_list, reverse=True))

    # timing start from 1
    timer = 1
    dfs_init()

    for index, time_info in enumerate(zip(d_time[1:], f_time[1:]), 1):
        print(index, *time_info)