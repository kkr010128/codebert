n = int(input())
s = input()
l = []

for i in s:
    l.append(chr((ord(i) - 65 + n) % 26 + 65))
print(*l, sep="")