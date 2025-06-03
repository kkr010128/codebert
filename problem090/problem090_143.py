s = input()
ans = 0
if s[0] == "R":
    ans += 1
    if s[1] == "R":
        ans += 1
        if s[2] == "R":
            ans += 1
elif s[1] == "R":
    ans += 1
    if s[2] == "R":
        ans += 1
elif s[2] == "R":
    ans += 1
print(ans)