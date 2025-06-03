# D - Maze Master
# https://atcoder.jp/contests/abc151/tasks/abc151_d
from collections import deque


def main():
    height, width = [int(num) for num in input().split()]
    maze = [input() for _ in range(height)]

    ans = 0
    next_to = ((0, 1), (1, 0), (0, -1), (-1, 0))

    for start_x in range(height):
        for start_y in range(width):
            if maze[start_x][start_y] == '#':
                continue
            queue = deque()
            queue.append((start_x, start_y))
            reached = [[-1] * width for _ in range(height)]
            reached[start_x][start_y] = 0

            while queue:
                now_x, now_y = queue.popleft()
                for move_x, move_y in next_to:
                    adj_x, adj_y = now_x + move_x, now_y + move_y
                    # Python は index = -1 が通ってしまうことに注意。
                    # except IndexError では回避できない。
                    if (not 0 <= adj_x < height
                            or not 0 <= adj_y < width
                            or maze[adj_x][adj_y] == '#'
                            or reached[adj_x][adj_y] != -1):
                        continue
                    queue.append((adj_x, adj_y))
                    reached[adj_x][adj_y] = reached[now_x][now_y] + 1
            most_distant = max(max(row) for row in reached)
            ans = max(most_distant, ans)
    print(ans)


if __name__ == '__main__':
    main()
