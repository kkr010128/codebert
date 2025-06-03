s = str(input())
t = ''
for c in s:
    if 65 <= ord(c) and ord(c) <= 90:
        t += c.lower()
    elif 97 <= ord(c) and ord(c) <= 122:
        t += c.upper()
    else:
        t += c
print(t)
