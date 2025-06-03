n = int(input())
s = input()
t = ''

for c in s:
    if ord(c) + n > ord('Z'):
        m = ord('Z') - ord(c)
        t += chr(ord('A') + (n - m - 1))
    else:
        t += chr(ord(c) + n)

print(t)
