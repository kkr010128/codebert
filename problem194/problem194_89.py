import sys

readline = sys.stdin.readline
inf = float('inf')

def main():
    H, W = map(int, readline().split())
    grid = []
    grid.append(['*'] * (W+2))
    for _ in range(H):
        grid.append(['*'] + list(readline()[:-1]) + ['*'])
    grid.append(['*']*(W+2))

    DP = [[inf] * (W+2) for _ in range(H+2)]
    DP[1][1] = (grid[1][1] == '#')*1

    for i in range(1, H+1):
        for j in range(1, W+1): 
            if i == 1 and j == 1:
                continue
            k = i
            gridkj = grid[k][j]
            if gridkj == '.':
                DP[k][j] = min(DP[k][j-1], DP[k-1][j])
            if gridkj == '#':
                DP[k][j] = min(DP[k][j-1]+(grid[k][j-1] in ['.', '*']), DP[k-1][j] + (grid[k-1][j] in ['.', '*']))
    ans = DP[H][W]
    print(ans)

if __name__ == "__main__":
    main()
