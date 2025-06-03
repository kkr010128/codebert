import sys
import copy
from collections import deque

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
#read = sys.stdin.buffer.read

def main():
    global field
    R, C, K = map(int, input().split())
    field = []
    for _ in range(R):
        tmp = [0] * C
        field.append(tmp)
    DP1 = copy.deepcopy(field)
    DP2 = copy.deepcopy(field)
    DP3 = copy.deepcopy(field)

    for _ in range(K):
        r, c, k = map(int, input().split())
        field[r-1][c-1] = k
    
    i = 0
    DP1[0][0] = field[0][0]
    for j in range(1, C):
        DP3[i][j] = max(DP2[i][j-1] + field[i][j], DP3[i][j-1])
        DP2[i][j] = max(DP1[i][j-1] + field[i][j], DP2[i][j-1])
        DP1[i][j] = max(field[i][j], DP1[i][j-1])

    for i in range(1, R):
        for j in range(C):
            DP3[i][j] = max(DP2[i][j-1] + field[i][j], DP3[i][j-1])
            DP2[i][j] = max(DP1[i][j-1] + field[i][j], DP2[i][j-1])
            DP1[i][j] = max(field[i][j], DP1[i][j-1], max(DP1[i-1][j], DP2[i-1][j], DP3[i-1][j]) + field[i][j])

    ans = max(DP3[R-1][C-1], DP2[R-1][C-1], DP1[R-1][C-1])
    print(ans)


if __name__ == "__main__":
    main()
