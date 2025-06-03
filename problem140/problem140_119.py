t = input()
ans = []
for i in t:
    if i == "?":
        i = "D"
    ans.append(i)

print("".join(ans))