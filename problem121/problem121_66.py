X = int(input())
d = {}
for i in range(0, 26):
    d[i+1] = chr(97+i)
a = []
while X > 0:
    if X%26 != 0:
        a.append(d[(X % 26)])
        X -= X % 26
    else:
        a.append(d[26])
        X -= 26
    X //= 26
for i in a[::-1]:
    print(i, end='')
print()