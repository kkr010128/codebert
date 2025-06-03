from math import floor
s = input()
k = int(input())
if len(set(s)) == 1:
    print(floor(len(s) * k / 2))
    exit(0)
x = s[0]
y = 1
ans = 0
for i in s[1:]:
    if i == x:
        y += 1
    else:
        ans += floor(y / 2)
        x = i
        y = 1
ans += floor(y / 2)
if s[0] != s[-1]:
    print(ans * k)
else:
    x = s[0]
    y = 1
    for i in s[1:]:
        if x == i:
            y += 1
        else:
            a = y
            break
    y = 0
    for i in s[::-1]:
        if x == i:
            y += 1
        else:
            b = y
            break
    print(ans * k - ((floor(a / 2) + floor(b / 2) - floor((a + b) / 2)) * (k - 1)))