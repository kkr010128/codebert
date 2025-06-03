n = int(input())
s = str(input())
w = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
t = ""
for i in range(len(s)):
    for h in range(26):
        if s[i] == w[h]:
            t += w[h+n]
            break
print(t)