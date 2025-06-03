N = int(input())
S = input()

s = list(S)
for i in range(len(S)):
    if (ord(s[i]) - 64 + N) % 26 == 0:
        p = 90
    else:
        p = (ord(s[i]) - 64 + N) % 26 + 64

    s[i] = chr(p)

print("".join(s))