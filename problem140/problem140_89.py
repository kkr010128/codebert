t = input()
n = len(t)
t += "a"
ans = ""
for i in range(n):
    if t[i] == "?":
        ans += "D"
    else:
        ans += t[i]
print(ans)