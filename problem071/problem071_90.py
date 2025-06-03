s = input()
l = []
for i in range(len(s)):
    l.append(s[i])
if l[len(l)-1] == "s":
    print(s+str("es"))
else:
    print(s+str("s"))
