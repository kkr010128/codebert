H,W,K=map(int,input().split())
c = []
ans = 0

for i in range(H):
    s =list(input())
    c.append(s)

for i in range(2**H):
    for j in range(2**W):
        tmp = 0
        for h in range(H):
            for w in range(W):
                if 2**h & i >0 and 2**w & j >0:
                    if c[h][w] == "#":
                        tmp += 1

        if tmp == K:
            ans += 1

print(ans)