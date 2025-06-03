text = raw_input()
t = list(text)
for i in range(len(t)):
    if t[i].isupper():
        t[i] = t[i].lower()
    elif t[i].islower():
        t[i] = t[i].upper()
print "".join(t)