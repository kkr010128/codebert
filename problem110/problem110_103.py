h, w, k = map(int, input().split())
A =[]
for i in range(h):
    a = input()
    A.append([a[i] == "#" for i in range(w)])
ans = 0
for bit in range(1 << h):
    for tib in range(1 << w):
        now = 0
        for i in range(h):
            for j in range(w):
                if(bit >> i) & 1 == 0 and (tib >> j) & 1 == 0 and A[i][j] == True: now += 1
        if now == k: ans += 1
print(ans)