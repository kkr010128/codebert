s = input()
t = ""
for i in range(len(s)):
    if s[i].islower():
        t += s[i].upper()
    elif s[i].isupper():
        t += s[i].lower()
    else:
        t += s[i]
print(t)

