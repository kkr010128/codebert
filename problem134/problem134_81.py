n = int(input())
n_l = list(map(int, input().split()))

VORDER = 10 ** 18
ans = 1

if 0 in n_l:
    ans = 0
else:
    for i in n_l:
        ans = i * ans
        if ans > VORDER:
            ans = -1
            break

print(ans)
