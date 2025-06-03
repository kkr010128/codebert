import collections

H, W, K = [int(x) for x in input().split()]
S = [input().strip() for _ in range(H)]

ans = float("inf")


for i in range(2 ** (H - 1)):
    bundan = {}
    bundan[0] = 0
    prev = 0
    tmp = 0
    for j in range(H - 1):
        if i >> j & 1 == 1:
            prev += 1
            bundan[j + 1] = prev
            tmp += 1
        else:
            bundan[j + 1] = prev

    c = collections.Counter()
    for kk in range(W):
        f = False
        for k in range(H):
            if f:
                break
            if S[k][kk] == '1':
                c[bundan[k]] += 1
                if c[bundan[k]] > K:
                    tmp += 1
                    f = True
                    c = collections.Counter()
                    for kkk in range(H):
                        if S[kkk][kk] == '1':
                            c[bundan[kkk]] += 1
                    break
    for k in c.keys():
        if c[k] > K:
            tmp = float("inf")
            break


    ans = min(ans, tmp)


print(ans)




