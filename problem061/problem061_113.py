s = input()

o = ""
for w in s:
    if w.isupper():
        o += w.lower()
    elif w.islower():
        o += w.upper()
    else:
        o += w
print(o)
