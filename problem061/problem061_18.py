s = raw_input()
r = ''
for c in s:
    d = c
    if c >= 'a' and c <= 'z':
        d = chr(ord(c) - ord('a') + ord('A'))
    if c >= 'A' and c <= 'Z':
        d = chr(ord(c) - ord('A') + ord('a'))
    r = r + d
print r