#import io, os
#input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

import sys
input = sys.stdin.buffer.readline

def main():
    R, C, K = map(int, input().split())
    A = [[0]*C for _ in range(R)]
    for i in range(K):
        r, c, v = map(int, input().split())
        r, c = r-1, c-1
        A[r][c] = v

    dp0 = [[0]*(C+1) for i in range(R+1)]
    dp1 = [[0]*(C+1) for i in range(R+1)]
    dp2 = [[0]*(C+1) for i in range(R+1)]
    dp3 = [[0]*(C+1) for i in range(R+1)]
    for i in range(R):
        for j in range(C):
            dp3[i][j] = max(dp3[i][j], dp2[i][j]+A[i][j])
            dp2[i][j] = max(dp2[i][j], dp1[i][j]+A[i][j])
            dp1[i][j] = max(dp1[i][j], dp0[i][j]+A[i][j])

            dp3[i][j+1] = max(dp3[i][j+1], dp3[i][j])
            dp2[i][j+1] = max(dp2[i][j+1], dp2[i][j])
            dp1[i][j+1] = max(dp1[i][j+1], dp1[i][j])
            dp0[i][j+1] = max(dp0[i][j+1], dp0[i][j])

            dp0[i+1][j] = max(dp0[i+1][j], dp0[i][j])
            dp0[i+1][j] = max(dp0[i+1][j], dp1[i][j])
            dp0[i+1][j] = max(dp0[i+1][j], dp2[i][j])
            dp0[i+1][j] = max(dp0[i+1][j], dp3[i][j])
    #print(dp)
    print(max([dp0[R-1][C-1], dp1[R-1][C-1], dp2[R-1][C-1], dp3[R-1][C-1]]))

if __name__ == '__main__':
    main()
