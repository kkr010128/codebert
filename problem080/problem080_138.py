def solve(xy):
    ans = 0
    pos = [xy[0] for _ in range(4)]

    for p in xy:
        if pos[0][0] + pos[0][1] < p[0] + p[1]:
            pos[0] = p
        if pos[1][0] + pos[1][1] > p[0] + p[1]:
            pos[1] = p
        if pos[2][0] - pos[2][1] < p[0] - p[1]:
            pos[2] = p
        if pos[3][0] - pos[3][1] > p[0] - p[1]:
            pos[3] = p

    return max(pos[0][0]+pos[0][1]-pos[1][0]-pos[1][1], pos[2][0]-pos[2][1]-pos[3][0]+pos[3][1])


if __name__ == "__main__":
    N = int(input())
    xy = [list(map(int, input().split())) for _ in range(N)]
    print(solve(xy))
