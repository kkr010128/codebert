#atcoder template
def main():
    import sys
    imput = sys.stdin.readline
    #文字列入力の時は上記はerrorとなる。
    #ここにコード
    #input
    N, S = map(int, input().split())
    A = list(map(int, input().split()))

    #output
    mod = 998244353
    dp = [[0] * ( S+1) for _ in range(N+1)]
    #dp[i, j]を、A[0]...A[i]までを使って、Tの空でない部分集合
    #{x_1, x_2, ..., x_k}であって、Ax_1 + A_x_2 + ... + A_x_k = jを満たすものの個数とする。
    dp[0][0] = 1
    #iまででjが作られている時、i+1ではA[i]がどのような値であっても、部分集合としてjは作れる。
    #iまででjが作られない時、j-A[i]が作られていれば、A[i]を足せばjは作れる。
    for i in range(N):
        for j in range(S+1):
            dp[i+1][j] += dp[i][j] * 2 
            dp[i+1][j] %= mod
            if j >= A[i]:
                dp[i+1][j] += dp[i][j-A[i]]
                dp[i+1][j] %= mod
                    
    print(dp[N][S] % mod)

    #N = 1のときなどcorner caseを確認！
if __name__ == "__main__":
    main()