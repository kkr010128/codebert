S = raw_input()
tmp = ''
for s in S:
    if s.isupper():
        tmp += s.lower()
    elif s.islower():
        tmp += s.upper()
    else:
        tmp += s
print tmp