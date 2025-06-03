n = int(input())
L = sorted(list(map(int,input().split())),reverse = True)
ans = 0
for i in L:
    for j in L:
        for k in L:
            if i<j<k:
                if i + j>k:
                    ans += 1
print(ans)