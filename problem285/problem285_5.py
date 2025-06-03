S = input()

ans = 0
l, r = 0, 0
i = 0
while i < len(S):
    while i < len(S) and S[i] == "<":
        l += 1
        i += 1
    while i < len(S) and S[i] == ">":
        r += 1
        i += 1
    ans += l * (l + 1) // 2
    ans += r * (r + 1) // 2
    ans -= min(l, r)
    l, r = 0, 0
print(ans)
