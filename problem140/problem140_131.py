a = input()
t = list(a)
if t[len(t)-1] == "?":
    t[len(t)-1] = "D"
if t[0] == "?":
    if t[1] == "D" or t[1] == "?":
        t[0] = "P"
    else:
        t[0] = "D"
for i in range(1, len(t)-1):
    if t[i] == "?" and t[i-1] == "P":
        t[i] = "D"
    elif t[i] == "?" and t[i+1] == "D":
        t[i] = "P"
    elif t[i] == "?" and t[i+1] == "?":
        t[i] = "P"
    elif t[i] == "?":
        t[i] = "D"

answer = "".join(t)
print(answer)