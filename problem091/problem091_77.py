N = int(input())
L = sorted(list(map(int, input().split())))
ans = 0
for i in L:
    for j in L:
        for k in L:
            if i < j < k:
                if i + j + k > max(i,j,k) * 2:
                    ans += 1
else:
    print(ans)