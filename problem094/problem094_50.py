def main(R,C,K,V):
    dp = [0]*(4*R*C)
    dp[1+4*0+4*C*0] = V[0][0]
    for k in range(4*R*C):
        n = k%4
        j = k//4%C
        i = k//(4*C)
        if n!=0:
            if i != 0 and n==1:
                dp[k] = max(dp[k-4*C-n:k-4*C-n+4])+V[i][j]
            if j != 0:
                dp[k] = max(dp[k],dp[k-4],dp[k-5]+V[i][j])
        if n==0:
            if i != 0:
                dp[k] = max(dp[k-4*C-n:k-4*C-n+4])

    print(max(dp[-5:-1]))

if __name__ == '__main__':
    R,C,K = map(int,input().split())
    C += 1
    rcv = [list(map(int,input().split())) for _ in range(K)]
    V = [[0]*C for _ in range(R)]
    for i in range(K):
        r,c,v = rcv[i]
        r -= 1
        c -= 1
        V[r][c] = v
    main(R,C,K,V)