s = input()
if s[0] == "R":
    if s[1] == "R":
        if s[2] == "R":
            ans = 3
        else:
            ans = 2
    else:
        ans = 1
else:
    if s[1] == "R":
        if s[2] == "R":
            ans = 2
        else:
            ans = 1
    elif s[2] == "R":
        ans = 1
    else:
        ans = 0
print(ans)