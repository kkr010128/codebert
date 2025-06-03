N = int(input())
s = list(input())

for i in range(len(s)):
    if ord(s[i])+N-ord('A') < 26:
        s[i] = chr(ord(s[i])+N)
    else:
        s[i] = chr(ord(s[i])+N-26)
print(''.join(s))