from itertools import product

H, W, K = map(int, input().split())
C = [list(input()) for _ in range(H)]

p1 = list(product([False, True], repeat=H))
p2 = list(product([False, True], repeat=W))
ans = 0

for i in range(len(p1)):
    for j in range(len(p2)):
        count = 0
        for a in range(H):
            for b in range(W):
                if C[a][b] == "#" and not p1[i][a] and not p2[j][b]:
                    count += 1
        if count == K:
            ans += 1
print(ans)