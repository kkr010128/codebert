str = raw_input()
li = []
for a in list(str):
    if a.islower():
        li.append(a.upper())
    elif a.isupper():
        li.append(a.lower())
    else:
        li.append(a)
print "".join(li)