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


def generate_adj_matrix(v_info):
    for v_detail in v_info:
        v_index, adj_num, *adj_list = map(int, v_detail)
        # assert len(adj_list) == adj_num
        init_adj_table[v_index].extend(adj_list)
    return init_adj_table


def graph_bfs(v_init):
    status[v_init] = VISITED_IN_QUEUE
    distance[v_init] = 0
    queue.appendleft(v_init)

    while queue:
        current = queue.popleft()
        for v in adj_table[current]:
            if status[v] is UNVISITED:
                status[v] = VISITED_IN_QUEUE
                distance[v] = distance[current] + 1
                queue.append(v)
        status[current] = POPPED_OUT
    return distance


if __name__ == '__main__':
    _input = sys.stdin.readlines()
    vertices_num = int(_input[0])
    vertices_info = list(map(lambda x: x.split(), _input[1:]))
    init_adj_table = [[] for _ in range(vertices_num + 1)]
    # assert len(vertex_info) == vertex_num

    # config length = (vertex_num + 1)
    queue = deque()
    status = [UNVISITED] * (vertices_num + 1)
    distance = [-1] * (vertices_num + 1)

    adj_table = generate_adj_matrix(vertices_info)
    ans = graph_bfs(1)
    for j in range(vertices_num):
        print(j + 1, ans[j + 1])