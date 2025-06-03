def solve():
    N,X,Y = [int(i) for i in input().split()]
    distance_cnt = {}
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            distance = min(j-i, abs(X-i)+abs(Y-j)+1)
            distance_cnt[distance] = distance_cnt.get(distance, 0) + 1
    for i in range(1, N):
        print(distance_cnt.get(i, 0))

if __name__ == "__main__":
    solve()