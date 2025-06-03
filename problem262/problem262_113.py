def main():
    N = int(input())
    comment = []

    for i in range(1, N + 1):
        A = int(input())
        for j in range(1, A + 1):
            c = [i]
            c.extend(list(map(int, input().split())))
            comment.append(c)

    ans = 0
    for i in range(1, 2**N):
        flg = True
        for h, t, c in comment:
            #発言者が正直者か
            if i & (1 << h - 1):
                #発言が適切か
                if ((i >> t - 1) & 0b1) ^ c:
                    flg = False
                    break
        
        if flg:
            tmp = 0
            for j in range(N):
                if i & (1 << j):
                    tmp += 1
            
            ans = max(ans, tmp)

    print(ans)


if __name__ == '__main__':
    main()