from itertools import product

h, w = map(int, input().split())
maze = [input() for _ in range(h)]


def neighbors(ih, iw):
    for ih1, iw1 in (
        (ih - 1, iw),
        (ih + 1, iw),
        (ih, iw - 1),
        (ih, iw + 1),
    ):
        if 0 <= ih1 < h and 0 <= iw1 < w and maze[ih1][iw1] == '.':
            yield (ih1, iw1)



def len_maze(ih, iw):
    # BFS
    if maze[ih][iw] == '#':
        return 0

    stepped = [[False] * w for _ in range(h)]
    q0 = [(ih, iw)]
    l = -1
    while q0:
        q1 = set()
        for ih0, iw0 in q0:
            stepped[ih0][iw0] = True
            for ih1, iw1 in neighbors(ih0, iw0):
                if not stepped[ih1][iw1]:
                    q1.add((ih1, iw1))
        q0 = list(q1)
        l += 1

    return l


answer = max(len_maze(ih, iw) for ih, iw in product(range(h), range(w)))
print(answer)
