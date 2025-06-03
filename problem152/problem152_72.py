import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
s = []
for _ in range(n):
    s.append(input())

inc = []
zeros = []
dec = []

for i, j in enumerate(s):
    minimum = 0
    now = 0
    for k in j:
        if k == "(":
            now += 1
        else:
            now -= 1
        minimum = min(minimum, now)
    if now > 0:
        inc.append([minimum, i])
    elif now < 0:
        dec.append([minimum - now, i])
    else:
        zeros.append([minimum, i])

inc.sort(reverse=True)
dec.sort()

now = 0

for i, j in inc:
    for k in s[j]:
        if k == "(":
            now += 1
        else:
            now -= 1
        if now < 0:
            print("No")
            sys.exit()
for i, j in zeros:
    for k in s[j]:
        if k == "(":
            now += 1
        else:
            now -= 1
        if now < 0:
            print("No")
            sys.exit()
for i, j in dec:
    for k in s[j]:
        if k == "(":
            now += 1
        else:
            now -= 1
        if now < 0:
            print("No")
            sys.exit()
ans = "Yes" if now == 0 else "No"
print(ans)
