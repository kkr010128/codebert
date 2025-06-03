n = int(input())

t, h = 0, 0

for i in range(n):
    s1, s2 = input().split()
    if s1 > s2:
        t += 3
    elif s1 < s2:
        h += 3
    else:
        t += 1
        h += 1

print(t, h)