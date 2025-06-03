line = raw_input()
line2 = ''
for s in line:
    if s == '\n':
        break
    elif s.islower():
        line2 += s.upper()
    elif s.isupper():
        line2 += s.lower()
    else:
        line2 += s
print line2