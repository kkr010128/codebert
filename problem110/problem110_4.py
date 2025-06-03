H, W, K = map(int, input().split())
table = []
ans = 0
for _ in range(H):
    li = input()
    table.append(li)
for i in range(2**H):
    for j in range(2**W):
        counter = 0
        for k in range(H):
            for l in range(W):
                if (i>>k)&1 and (j>>l)&1 and table[k][l] == "#":
                    counter += 1
        if counter == K:
            ans += 1
print(ans)
