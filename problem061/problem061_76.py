from sys import stdin

s = list(stdin.readline())
for i in range(len(s)):
    if s[i].islower():
        s[i] = s[i].upper()
    elif s[i].isupper():
        s[i] = s[i].lower()

print(*s, sep="", end="")
