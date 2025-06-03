def main():
    N = int(input())
    n = str(N)
    
    cnt = [[0] * (10) for _ in range(10)]
    
    for i in range(1, N+1):
        a = int(str(i)[0])
        b = i%10
        cnt[a][b] += 1
    ans = 0
    for i in range(1, 10):
        for j in range(1, 10):
            ans += cnt[i][j]*cnt[j][i]
    print(ans)
main()