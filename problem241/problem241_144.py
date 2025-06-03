from queue import Queue
def isSafe(row, col):
    return row >= 0 and col >= 0 and row<h and col<w and mat[row][col] != '#'


def bfs(row, col):
    visited = [[False]*w for _ in range(h)]
    que = Queue()
    dst = 0
    que.put([row, col, 0])
    visited[row][col] = True
    moves = [[-1, 0],[1, 0], [0, -1], [0, 1]]
    while not que.empty():
        root = que.get()
        row, col, dst = root
        for nrow, ncol in moves:
            row2 = row + nrow
            col2 = col + ncol 
            if isSafe(row2, col2) is True and visited[row2][col2] is False:
                visited[row2][col2] = True
                que.put([row2, col2, dst+1])
                 
    return dst 

h, w = map(int, input().split())
mat = [input() for _ in range(h)]
ans = 0
for row in range(h):
    for col in range(w):
        if mat[row][col] == '.':
            ans = max(ans, bfs(row, col))

print(ans)

