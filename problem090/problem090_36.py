lst = list(input())

tmp = 0
ans = 0

for i in lst:
    if i == "R":
        tmp = tmp + 1
        ans = max(ans, tmp)
    else:
        tmp = 0

print(ans)