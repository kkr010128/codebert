t = input()
s = [i for i in t]
if s[0] == "?":
    s[0] = "D"
for i in range(1, len(t) - 1):
    if s[i] == "?":
        if s[i-1] == "D" and s[i+1] == "D":
            s[i] = "P"
        elif s[i-1] == "D" and s[i+1] == "?":
            s[i] = "P"
        else:
            s[i] = "D"
if s[-1] == "?":
    s[-1] = "D"
print("".join(s))