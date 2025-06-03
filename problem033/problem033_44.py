u, s, e, w, n, d = input().split()
t = input()
for i in t:
    if i == 'N':
        u, s, n, d = s, d, u, n
    elif i == 'E':
        u, e, w, d = w, u, d, e
    elif i == 'S':
        u, s, n, d = n, u, d, s
    elif i == 'W':
        u, e, w, d = e, d, u, w
print(u)