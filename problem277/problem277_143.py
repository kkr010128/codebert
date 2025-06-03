import sys
input = sys.stdin.readline


def main():
    H, W, K = map(int, input().split())
    cake = [[0]*W for _ in range(H)]
    sb = []
    for y in range(H):
        s = input().strip()
        for x, c in enumerate(s):
            if c == "#":
                sb.append((y, x))
    for i, (y, x) in enumerate(sb):
        cake[y][x] = i+1

    import collections
    for i, s in enumerate(sb):
        Q = collections.deque()
        Q.appendleft(s[1])
        y = s[0]
        while Q:
            x = Q.pop()
            if x-1 >= 0 and cake[y][x-1] == 0:
                cake[y][x-1] = i+1
                Q.appendleft(x-1)
            if x+1 <= W-1 and cake[y][x+1] == 0:
                cake[y][x+1] = i+1
                Q.appendleft(x+1)

    for y in range(1, H):
        for x in range(W):
            if cake[y][x] == 0:
                cake[y][x] = cake[y-1][x]
    for y in range(H-2, -1, -1):
        for x in range(W):
            if cake[y][x] == 0:
                cake[y][x] = cake[y+1][x]

    for c in cake:
        print(*c)


if __name__ == '__main__':
    main()
