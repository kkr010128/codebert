N = int(input())
S = list(input())

l = []
for i in S:
    if ord(i)+N > 90:
        l.append(chr(64+(ord(i)+N)%90))
    else:
        l.append(chr(ord(i)+N))

print("".join(l))