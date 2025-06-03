from sys import stdin


def chmin(a,b):
    if a > b: return b
    else: return a


def chmax(a,b):
    if a < b: return b
    else: return a


if __name__ == "__main__":
    _in = [_.rstrip() for _ in stdin.readlines()]
    N = int(_in[0])  # type:int
    A_arr = list(map(int,_in[1].split(' ')))  # type:list(int)
    # vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    A_arr_wloc = []
    for i,A in enumerate(A_arr):
        A_arr_wloc.append([A,i])
    A_arr_wloc.sort(reverse=True)
    dp = [[0] * (N+1) for _ in range(N+1)]
    for i in range(N):
        for j in range(N-i):
            dp[i+1][j] = chmax(dp[i+1][j], dp[i][j]+A_arr_wloc[i+j][0]*(A_arr_wloc[i+j][1]-i)) # left
            dp[i][j+1] = chmax(dp[i][j+1], dp[i][j]+A_arr_wloc[i+j][0]*((N-1-j)-A_arr_wloc[i+j][1])) # right
    cnt = 0
    for i in range(0,N+1):
        cnt = chmax(cnt, dp[i][N-i])
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    print(cnt)
