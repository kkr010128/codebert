T = input()

res = ""
for t in T:
    if t == "?":
        res += "D"
    else:
        res += t

print(res)