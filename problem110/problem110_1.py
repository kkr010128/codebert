H,W,K = map(int,input().split())
ans = 0
C = []
for i in range(H):
    c = list(input())
    C.append(c)
for Is in range(1<<H):
    for Js in range(1<<W):
        count = 0
        for i in range(H):
            for j in range(W):
                if Is>>i&1:
                    continue
                if Js >>j&1:
                    continue
                if C[i][j] == "#":
                    count +=1
        if count == K:
            ans += 1
print(ans)