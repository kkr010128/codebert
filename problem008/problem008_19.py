from typing import List


def dfs(adj_matrix: List[List[int]], vartex: int) -> int:
    global step
    global discover_times
    global finish_times
    if 0 != discover_times[vartex]:
        return 0
    discover_times[vartex] = step

    for col_idx in range(len(adj_matrix)):
        if (0 != adj_matrix[vartex][col_idx]) and (0 == discover_times[col_idx]):
            step += 1
            dfs(adj_matrix, col_idx)

    step += 1
    finish_times[vartex] = step

    return 1


if __name__ == "__main__":
    num_vertices = int(input())
    adj_matrix = [[0] * num_vertices for i in range(num_vertices)]

    for _ in range(num_vertices):
        vertex, _, *adjs = map(lambda x: int(x), input().split())
        for adj in adjs:
            adj_matrix[vertex - 1][adj - 1] = 1

    step = 1
    discover_times = [0] * num_vertices
    finish_times = [0] * num_vertices

    for vartex in range(num_vertices):
        if 1 == dfs(adj_matrix, vartex):
            step += 1

    for vertex, (d, f) in enumerate(zip(discover_times, finish_times)):
        print(f"{vertex + 1} {d} {f}")

