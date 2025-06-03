s = input()
t = input()
ans = 0
for cs, ct in zip(s, t):
    if cs != ct:
        ans += 1
print(ans)