import sys
import itertools
import collections


def search(H, W, S, start):
    wall_i = ord(b'#')
    used = [[-1 for h in range(W)] for w in range(H)]

    qu = collections.deque()
    qu.append(start)
    used[start[0]][start[1]] = 0

    while qu:
        h, w = qu.popleft()
        cost = used[h][w]
        for h0, w0 in ((h - 1, w), (h + 1, w), (h, w - 1), (h, w + 1)):
            if not (0 <= h0 < H and 0 <= w0 < W):
                continue
            if used[h0][w0] != -1:
                continue
            if S[h0][w0] == wall_i:
                continue

            used[h0][w0] = cost + 1
            qu.append((h0, w0))

    return max(cost for costs in used for cost in costs)


def resolve(in_):
    H, W = map(int, next(in_).split())
    S = tuple(s.strip() for s in itertools.islice(in_, H))

    road_i = ord(b'.')

    roads = []
    for h in range(H):
        for w in range(W):
            if S[h][w] == road_i:
                roads.append((h, w))
    
    ans = max(search(H, W, S, start) for start in roads)
    
    return ans


def main():
    answer = resolve(sys.stdin.buffer)
    print(answer)


if __name__ == '__main__':
    main()
