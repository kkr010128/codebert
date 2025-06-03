s = input()
t = list(s)
for i in range(len(t)):
    if t[i].islower() == True:
        t[i] = t[i].upper()
    elif t[i].isupper() == True:
        t[i] = t[i].lower()
print("".join(t))