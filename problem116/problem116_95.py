s = input()
t = input()
l = len(s)
x = 0
for i in range(l):
    if s[i] != t[i]:
        x += 1
print(x)