def main():
    H, W, K = map(int, input().split())
    chocolate = [list(map(int,list(input()))) for _ in range(H)]
    choco = [[0]*W for _ in range(H)]
    ids = [0] * H
    ans = 10 ** 9
    for bit in range(1<<(H-1)):
        group_id = 0
        for i in range(H):
            ids[i] = group_id
            if (bit>>i)&1:
                group_id += 1
        group_id += 1
        
        for i in range(group_id):
            for j in range(W):
                choco[i][j] = 0

        for i in range(H):
            for j in range(W):
                choco[ids[i]][j] += chocolate[i][j]
        
        if any(choco[i][j] > K for i in range(group_id) for j in range(W)):
            continue
        
        num = group_id - 1
        now = [0] * group_id
        def add(j):
            for i in range(group_id):
                now[i] += choco[i][j]
            if any(now[i] > K for i in range(group_id)):
                return False
            else:
                return True

        for j in range(W):
            if not add(j):
                num += 1
                now = [0] * group_id
                add(j)
        ans = min(ans, num)
    print(ans)


if __name__ == "__main__":
    main()