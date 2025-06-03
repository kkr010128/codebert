s = list(input())
c = 0
x = s[::-1]
for i in range(len(s)):
    if s[i] != x[i]:
        x[i] = s[i]
        c += 1
        s[::-1] = x
print(c)