N = int(input())
c = list(str(input()))
r = c.count('R')
w = 0
for i in range(r):
    if c[i] == 'W':
        w += 1
print(w)