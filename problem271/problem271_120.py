n = int(input())
s = input()
t = ''
for c in s:
    t += chr((ord(c) + n - 65) % 26 + 65 )
print(t)