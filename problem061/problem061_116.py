s = input()
u = s.upper()
l = s.lower()
a = []
for i in range(len(s)):
    if s[i] == u[i]:
        a.append(l[i])
    else:
        a.append(u[i])
print("".join(a))