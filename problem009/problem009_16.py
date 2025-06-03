#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
input:
4
1 2 2 4
2 1 4
3 0
4 1 3

output:
1 0
2 1
3 2
4 1
"""

import sys
from collections import deque

UNVISITED, VISITED_IN_QUEUE, POPPED_OUT = 0, 1, 2


def graph_bfs(v_init):
    queue = deque()
    status[v_init] = VISITED_IN_QUEUE
    distance[v_init] = 0
    queue.appendleft(v_init)

    while queue:
        current = queue.popleft()
        for adj in adj_table[current]:
            if status[adj] is UNVISITED:
                status[adj] = VISITED_IN_QUEUE
                distance[adj] = distance[current] + 1
                queue.append(adj)
        status[current] = POPPED_OUT
    return None


if __name__ == '__main__':
    _input = sys.stdin.readlines()
    v_num = int(_input[0])
    vertices = list(map(lambda x: x.split(), _input[1:]))
    # assert len(vertex_info) == vertex_num

    status = [UNVISITED] * (v_num + 1)
    distance = [-1] * (v_num + 1)

    adj_table = tuple([] for _ in range(v_num + 1))
    for v_info in vertices:
        v_index, adj_num, *adj_list = map(int, v_info)
        # assert len(adj_list) == adj_num
        adj_table[v_index].extend(adj_list)

    graph_bfs(v_init=1)
    for index, v in enumerate(distance[1:], 1):
        print(index, v)