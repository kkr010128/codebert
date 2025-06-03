t = list(input())
t.reverse()

tmptmp = "P"
for i in range(len(t)):
    if i == 0:
        tmp = t[i]
        continue
    if tmp == "?" and tmptmp != "D":
        t[i-1] = "D"
    elif tmp == "?" and tmptmp == "D" and t[i] != "D":
        t[i-1] = "D"
    elif tmp == "?" and tmptmp == "D" and t[i] == "D":
        t[i-1] = "P"
    tmptmp = t[i-1]
    tmp = t[i]

t.reverse()

if len(t) > 1:
    if t[0] == "?" and t[1] == "D":
        t[0] = "P"
    elif t[0] == "?" and t[1] == "P":
        t[0] = "D"

if len(t) == 1:
    t[0] = "D"

t = "".join(t)
print(t)
