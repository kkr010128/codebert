s = input()
n = ans = 0
for c in s:
    if c == "S":
        n = 0
        continue
    n += 1
    if n > ans:
        ans = n
print(ans)