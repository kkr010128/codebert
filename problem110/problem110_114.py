def main():
    H, W, K = map(int, input().split())
    c = [input() for _ in range(H)]
    ans = 0

    # 選ばない:0  選ぶ:1

    for row in range(2 ** H):
        for column in range(2 ** W):
            cnt = 0
            for i in range(H):
                for j in range(W):
                    if row >> i & 1:
                        continue
                    if column >> j & 1:
                        continue
                    if c[i][j] == "#":
                        cnt += 1
            if cnt == K:
                ans += 1
    print(ans)


if __name__ == "__main__":
    main()
