s = input()
t = ''
for i in range(0, len(s)):
    if s[i] == '?':
        t += 'D'
    else:
        t += s[i]
print(t)
