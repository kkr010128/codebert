s = raw_input()
ans = ""
for x in xrange(len(s)):
    if s[x].islower():
        ans += s[x].upper()
    else:
        ans += s[x].lower()
print ans