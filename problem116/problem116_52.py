s = input()
g = input()
m = 0
n = len(s)
if s == g:
    m = 0
else:
    for i in range(n):
        if s[i] == g[i]:
            continue
        else:
            m += 1

print(m)