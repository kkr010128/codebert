import numpy as np
from numba import njit
def main():
    R, C, K = map(int, input().split())
    field = np.full((R+1,C+1), 0, dtype='int64')
    dpt = np.full((R+1,C+1,4), 0, dtype='int64')
    for i in range(K):
        r, c, v = map(int, input().split())
        field[r][c] = v
    dp(R, C, field, dpt)
    print(max(dpt[-1][-1]))

@njit('i4(i4,i4,i8[:,:],i8[:,:,:])', cache=True)
def dp(R, C, field, dpt):
    for r in range(1, R+1):
        for c in range(1, C+1):
            for taken in range(4):
                max_v = 0
                if taken == 0:
                    max_v = max(dpt[r-1][c])
                    max_v = max(dpt[r][c-1][0], max_v)
                elif taken == 1:
                    max_v = max(dpt[r][c-1][taken-1] + field[r][c],
                                dpt[r][c-1][taken],
                                max(dpt[r-1][c]) + field[r][c])
                else:
                    max_v = max(dpt[r][c-1][taken-1] + field[r][c],
                                dpt[r][c-1][taken])
                dpt[r][c][taken] = max_v
    return 1

if __name__ == '__main__':
    main()
