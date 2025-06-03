s = input()
p = input()
found = False
for i in range(len(s)):
    ring = s[i:] + s[:i]
    if p in ring:
        print('Yes')
        found = True
        break
if not found:
    print('No')