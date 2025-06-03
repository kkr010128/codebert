from string import ascii_lowercase, ascii_uppercase
s = input()
t = ''
for i in s:
    if i in ascii_uppercase:
        t += i.lower()
    elif i in ascii_lowercase:
        t += i.upper()
    else:
        t += i
print(t)
