s = input()

if s[len(s)-1] == 's':
    s = s + 'es'
elif s[len(s)-1] != 's':
    s = s + 's'

print(s)
