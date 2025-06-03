N, M = map(int, input().split())

parent = [-1] * N


def get_group_root(x):
    if parent[x] < 0:
        return x
    return get_group_root(parent[x])


for i in range(0, M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1

    groupA = get_group_root(A)
    groupB = get_group_root(B)

    if groupA == groupB:
        continue
    elif parent[groupA] < parent[groupB]:
        parent[groupB] = A
        parent[groupA] -= 1
    else:
        parent[groupA] = B
        parent[groupB] -= 1


def check(x):
    return x < 0


print(sum(list(map(check, parent))) - 1)
