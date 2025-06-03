def main():
    H, W, K = (int(i) for i in input().split())
    A = [input() for i in range(H)]
    ans = [[-1]*W for _ in range(H)]
    p = 1
    for h in range(H):
        flag = False
        cnt = 0
        for w in range(W):
            if A[h][w] == "#":
                flag = True
                cnt += 1
        upper = p + cnt
        if not(flag):
            continue
        for w in range(W):
            ans[h][w] = p
            if A[h][w] == "#":
                if p + 1 < upper:
                    p += 1
        p = upper
    for h in range(H):
        for w in range(W):
            if ans[h][w] != -1:
                continue
            if h != 0:
                ans[h][w] = ans[h-1][w]
    for h in range(H)[::-1]:
        for w in range(W):
            if ans[h][w] != -1:
                continue
            if h != H-1:
                ans[h][w] = ans[h+1][w]
    for a in ans:
        print(*a)


if __name__ == '__main__':
    main()
