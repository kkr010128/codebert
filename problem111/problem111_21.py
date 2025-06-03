N = int(input())
table = sorted(list(map(int, input().split())), reverse=True)
ans = table[0]
rst = N - 2

for ti in table[1:]:
    if rst == 0:
        break
    if rst == 1:
        ans = ans + ti
        break
    ans = ans + 2 * ti
    rst = rst - 2

print(ans)
