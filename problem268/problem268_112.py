n = int(input())
a = [int(i) for i in input().split()]
color = [0, 0, 0]
ans = 1
mod = 10 ** 9 + 7
for i in a:
    cnt = color.count(i)
    ans *= cnt
    ans = ans % mod
    if ans > 0:
        color[color.index(i)] += 1
    else:
        break
print(ans)