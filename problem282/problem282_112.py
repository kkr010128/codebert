import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

def main():
    N,T,*ab = map(int, read().split())

    AB = []
    for a, b in zip(*[iter(ab)]*2):
        AB.append((a, b))

    AB.sort()
    
    dp = [[0] * (T+1) for _ in range(N+1)]

    ans = 0
    for i in range(N):
        w_i, v_i = AB[i]
        for j in range(T):
            if j < w_i:
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = max(dp[i][j - w_i] + v_i, dp[i][j])
        
        ans = max(ans, dp[i][T-1] + v_i)
    
    print(ans)
    

if __name__ == "__main__":
    main()
