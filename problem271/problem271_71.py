n = int(input())
s = list(input())
for i, char in enumerate(s):
    x = ord(char) + n
    if x > 90:
        x = x - 90 + 64
    s[i] = chr(x)

print("".join(s))