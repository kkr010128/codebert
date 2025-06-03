str = raw_input()
li = []

for c in list(str):
    if c.isupper():
        li.append(c.lower())
    elif c.islower():
        li.append(c.upper())
    else:
        li.append(c)
print ''.join(li)