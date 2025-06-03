K = int(input())
ans = -1
keep = 0
check = 7
for i in range(K):
    keep = (keep + check) % K
    if keep == 0:
        ans = i + 1
        break
    check = (check * 10) % K
print(ans)