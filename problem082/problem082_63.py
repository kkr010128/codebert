s = input()
n = len(s)
t = input()
m = len(t)
c_max = 0
for i in range(n - m + 1):
    c = 0
    for j in range(m):
        if s[i + j] == t[j]:
            c += 1
    if c > c_max:
        c_max = c
print(m - c_max)