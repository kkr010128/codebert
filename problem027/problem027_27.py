def inner_prod(v0, v1):
    ans = 0
    for x0, x1 in zip(v0, v1):
        ans += x0 * x1
    return ans


def vector_add(v0, v1):
    return [x0 + x1 for x0, x1 in zip(v0, v1)]


def vector_mul(vector, scaler):
    return [scaler * x for x in vector]


def matrix_mul(matrix, vector):
    ans = []
    for row in matrix:
        ans.append(inner_prod(row, vector))
    return ans


def koch(p0, p1, max_depth, depth=0):
    from math import sin, cos, pi

    if depth == max_depth:
        return []
    R = [[cos(pi / 3), -sin(pi / 3)], [sin(pi / 3), cos(pi / 3)]]
    p2 = vector_add(vector_mul(p0, 2 / 3), vector_mul(p1, 1 / 3))
    p3 = vector_add(vector_mul(p0, 1 / 3), vector_mul(p1, 2 / 3))
    p4 = vector_add(p2, matrix_mul(R, vector_add(p3, vector_mul(p2, -1))))
    return [
        koch(p0, p2, max_depth, depth + 1),
        p2,
        koch(p2, p4, max_depth, depth + 1),
        p4,
        koch(p4, p3, max_depth, depth + 1),
        p3,
        koch(p3, p1, max_depth, depth + 1),
    ]


def dfs_print(array):
    if not array:
        return
    if isinstance(array[0], int) or isinstance(array[0], float):
        print(*array)
    else:
        for child in array:
            dfs_print(child)


n = int(input())
result = [[0, 0], koch([0, 0], [100, 0], n), [100, 0]]
dfs_print(result)

